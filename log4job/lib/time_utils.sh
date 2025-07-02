#!/bin/bash

convert_to_seconds() {
    local time_str="$1"
    IFS=: read -r h m s <<< "$time_str"
    echo $((10#$h * 3600 + 10#$m * 60 + 10#$s))
}

format_duration() {
    local seconds="$1"
    printf "%02d:%02d:%02d" $((seconds / 3600)) $(((seconds % 3600) / 60)) $((seconds % 60))
}

handle_day_wraparound() {
    local start_sec="$1"
    local end_sec="$2"
    if (( end_sec < start_sec )); then
        end_sec=$((end_sec + 86400))
    fi
    echo "$end_sec"
}
