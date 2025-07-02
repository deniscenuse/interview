#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/time_utils.sh"
source "$SCRIPT_DIR/report_writer.sh"

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

    while IFS=',' read -r time name event pid; do
        key="${name}_${pid}"

        if [[ $event == "START" ]]; then
            start_times["$key"]="$time"
            job_names["$key"]="$name"
        elif [[ $event == "END" ]]; then
            start_time="${start_times[$key]}"
            [[ -z "$start_time" ]] && continue

            start_sec=$(convert_to_seconds "$start_time")
            end_sec=$(convert_to_seconds "$time")
            end_sec=$(handle_day_wraparound "$start_sec" "$end_sec")

            duration=$((end_sec - start_sec))
            duration_fmt=$(format_duration "$duration")

            if (( duration > 600 )); then
                write_report_line "error" "${job_names[$key]}" "$pid" "$start_time" "$time" "$duration_fmt" "$error_file" "$source_file"
            elif (( duration > 300 )); then
                write_report_line "warning" "${job_names[$key]}" "$pid" "$start_time" "$time" "$duration_fmt" "$warning_file" "$source_file"
            else
                write_report_line "clean" "${job_names[$key]}" "$pid" "$start_time" "$time" "$duration_fmt" "$clean_file" "$source_file"
                echo ${job_names[$key]}
            fi

            unset start_times["$key"]
            unset job_names["$key"]
        fi
    done < "$input_file"
}
