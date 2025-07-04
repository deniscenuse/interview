#!/usr/bin/env python3

import os
from lib.time_utils import get_timestamp
from lib.report_writer import prepare_report_files, write_no_files_found
from lib.job_processor import process_job_file
from lib.file_utils import archive_input_file

# 📁 Directories
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(ROOT_DIR, "input")
ARCHIVE_DIR = os.path.join(ROOT_DIR, "archive")
OUTPUT_DIR = os.path.join(ROOT_DIR, "output")

# 🕒 Timestamp and output dir for this run
timestamp = get_timestamp()
run_output_dir = os.path.join(OUTPUT_DIR, timestamp)
os.makedirs(run_output_dir, exist_ok=True)
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(ARCHIVE_DIR, exist_ok=True)

# 📝 Always prepare CSVs with headers
prepare_report_files(run_output_dir, timestamp)

# 🔍 Find .log files in input
input_files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".log")]

if not input_files:
    print("⚠️ No .log files found in input/. Reports generated with notice.")
    for level in ["warning", "error", "clean"]:
        write_no_files_found(level, run_output_dir, timestamp)
else:
    for filename in input_files:
        full_path = os.path.join(INPUT_DIR, filename)
        source_name = os.path.splitext(filename)[0]
        print(f"📄 Processing {filename}")
        process_job_file(full_path, run_output_dir, timestamp, source_name)
        archive_input_file(full_path, ARCHIVE_DIR, timestamp)

    print(f"✅ Reports generated in: {run_output_dir}")
