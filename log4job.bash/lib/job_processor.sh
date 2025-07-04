#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/time_utils.sh"
source "$SCRIPT_DIR/report_writer.sh"

# Helper: trim leading/trailing whitespace
trim() {
    echo -e "$1" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//'
}

process_job_file() {
    local input_file="$1"
    local output_dir="$2"
    local timestamp="$3"
    local source_file="$4"

    declare -A start_times
    declare -A job_names

    local warning_file="$output_dir/${timestamp}_warnings.csv"
    local error_file="$output_dir/${timestamp}_errors.csv"
    local clean_file="$output_dir/${timestamp}_clean.csv"

    echo "Processing file: $input_file" >> "$DEBUG_LOG"

    while IFS=',' read -r time name event pid; do
        echo "Raw line: $time, $name, $event, $pid" >> "$DEBUG_LOG"

        # trim whitespace
        time="$(trim "$time")"
        name="$(trim "$name")"
        event="$(trim "$event")"
        pid="$(trim "$pid")"

        key="${name}_${pid}"

        echo "Parsed line: time=$time name=$name event=$event pid=$pid key=$key" >> "$DEBUG_LOG"

        if [[ $event == "START" ]]; then
            echo "START event for key: $key at $time" >> "$DEBUG_LOG"
            start_times["$key"]="$time"
            job_names["$key"]="$name"

        elif [[ $event == "END" ]]; then
            echo "END event for key: $key at $time" >> "$DEBUG_LOG"
            start_time="${start_times[$key]}"
            if [[ -z "$start_time" ]]; then
                echo "⚠️ No matching START found for key: $key — skipping" >> "$DEBUG_LOG"
                continue
            fi

            start_sec=$(convert_to_seconds "$start_time")
            end_sec=$(convert_to_seconds "$time")
            end_sec=$(handle_day_wraparound "$start_sec" "$end_sec")

            duration=$((end_sec - start_sec))
            duration_fmt=$(format_duration "$duration")

            echo "Computed duration for key: $key — $duration seconds ($duration_fmt)" >> "$DEBUG_LOG"

            if (( duration > 600 )); then
                write_report_line "error"  "${job_names[$key]}" "$pid" "$start_time" "$time" "$duration_fmt" "$error_file" "$source_file"
                echo "Wrote ERROR record for $key" >> "$DEBUG_LOG"
            elif (( duration > 300 )); then
                write_report_line "warning" "${job_names[$key]}" "$pid" "$start_time" "$time" "$duration_fmt" "$warning_file" "$source_file"
                echo "Wrote WARNING record for $key" >> "$DEBUG_LOG"
            else
                write_report_line "clean"   "${job_names[$key]}" "$pid" "$start_time" "$time" "$duration_fmt" "$clean_file" "$source_file"
                echo "Wrote CLEAN record for $key" >> "$DEBUG_LOG"
            fi

            unset start_times["$key"]
            unset job_names["$key"]
        else
            echo "⚠️ Unknown event type: $event for key: $key" >> "$DEBUG_LOG"
        fi

    done < "$input_file"
}
