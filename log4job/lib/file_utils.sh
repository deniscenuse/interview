#!/bin/bash

archive_input_file() {
    local input_path="$1"
    local archive_dir="$2"
    local timestamp="$3"
    local basename="$(basename "$input_path")"
    mv "$input_path" "$archive_dir/logs_${timestamp}_$basename"
}
