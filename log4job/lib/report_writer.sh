#!/bin/bash

prepare_report_files() {
    local output_dir="$1"
    local ts="$2"
    mkdir -p "$output_dir"
    echo "level,name,pid,start_time,end_time,duration,source_file" > "$output_dir/${ts}_warnings.csv"
    echo "level,name,pid,start_time,end_time,duration,source_file" > "$output_dir/${ts}_errors.csv"
    echo "level,name,pid,start_time,end_time,duration,source_file" > "$output_dir/${ts}_clean.csv"
}

write_report_line() {
    local level="$1"
    local name="$2"
    local pid="$3"
    local start="$4"
    local end="$5"
    local duration="$6"
    local file="$7"
    local source="$8"
    echo "$level,$name,$pid,$start,$end,$duration,$source" >> "$file"
}
