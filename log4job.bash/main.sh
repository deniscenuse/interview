#!/bin/bash

set -e

# Load libraries
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/lib/time_utils.sh"
source "$SCRIPT_DIR/lib/report_writer.sh"
source "$SCRIPT_DIR/lib/job_processor.sh"

# Set paths
ROOT_DIR="$(pwd)"
INPUT_DIR="$ROOT_DIR/input"
ARCHIVE_DIR="$ROOT_DIR/archive"
OUTPUT_BASE="$ROOT_DIR/output"

# Get timestamp and create output dir
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
OUTPUT_DIR="$OUTPUT_BASE/$TIMESTAMP"
mkdir -p "$ARCHIVE_DIR"

DEBUG_LOG="$OUTPUT_DIR/debug.log"

# If argument provided, process only that file
if [[ -n "$1" ]]; then
    FILE="$1"
    if [[ ! -f "$FILE" ]]; then
        echo "Specified file '$FILE' not found."
        exit 1
    fi

    mkdir -p "$OUTPUT_DIR"
    prepare_report_files "$OUTPUT_DIR" "$TIMESTAMP"

    BASENAME=$(basename "$FILE" .log)
    echo "Processing $FILE as $BASENAME" >> "$DEBUG_LOG"
    process_job_file "$FILE" "$OUTPUT_DIR" "$TIMESTAMP" "$BASENAME"
    mv "$FILE" "$ARCHIVE_DIR/"

else
    # Check if there are any log files in input dir
    LOG_FILES=("$INPUT_DIR"/*.log)
    if [[ ! -e "${LOG_FILES[0]}" ]]; then
        echo "No reports generated as no input files were found."
        exit 0
    fi

    mkdir -p "$OUTPUT_DIR"
    prepare_report_files "$OUTPUT_DIR" "$TIMESTAMP"

    # Process all *.log files in input dir
    for FILE in "$INPUT_DIR"/*.log; do
        [[ -e "$FILE" ]] || continue
        echo "Found log file: $FILE" >> "$DEBUG_LOG"
        BASENAME=$(basename "$FILE" .log)
        echo "Processing $FILE as $BASENAME" >> "$DEBUG_LOG"
        process_job_file "$FILE" "$OUTPUT_DIR" "$TIMESTAMP" "$BASENAME"
        mv "$FILE" "$ARCHIVE_DIR/"
    done
fi

echo "Reports generated in: $OUTPUT_DIR"
