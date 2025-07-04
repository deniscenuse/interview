#!/usr/bin/env python3

import os
import sys
import datetime

# ✅ Ensure 'lib' directory is in the Python path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LIB_DIR = os.path.join(SCRIPT_DIR, 'lib')
sys.path.insert(0, LIB_DIR)

# ✅ Import from local modules inside lib/
from time_utils import get_timestamp
from report_writer import prepare_report_files
from job_processor import process_job_file
from file_utils import archive_input_file

# 🛠️ Setup directories
ROOT_DIR = os.getcwd()
INPUT_DIR = os.path.join(ROOT_DIR, 'input')
ARCHIVE_DIR = os.path.join(ROOT_DIR, 'archive')
OUTPUT_BASE_DIR = os.path.join(ROOT_DIR, 'output')

# 🕒 Timestamp for this run
timestamp = get_timestamp()
OUTPUT_DIR = os.path.join(OUTPUT_BASE_DIR, timestamp)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(ARCHIVE_DIR, exist_ok=True)

# 🪵 Debug log (optional)
debug_log_path = os.path.join(OUTPUT_DIR, "debug.log")
with open(debug_log_path, 'w') as debug_log:

    # 📄 Single file passed as argument
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        if not os.path.isfile(input_file):
            debug_log.write(f"❌ Input file not found: {input_file}\n")
            sys.exit(1)
        source_name = os.path.splitext(os.path.basename(input_file))[0]
        debug_log.write(f"📄 Processing {input_file} as {source_name}\n")

        prepare_report_files(OUTPUT_DIR, timestamp)
        process_job_file(input_file, OUTPUT_DIR, timestamp, source_name)
        archive_input_file(input_file, ARCHIVE_DIR, timestamp)

    else:
        # 📂 Process all .log files from input/
        log_files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".log")]
        if not log_files:
            debug_log.write("⚠️ No .log files found in input/\n")
            sys.exit(0)

        prepare_report_files(OUTPUT_DIR, timestamp)

        for filename in log_files:
            full_path = os.path.join(INPUT_DIR, filename)
            source_name = os.path.splitext(filename)[0]
            debug_log.write(f"📄 Processing {full_path} as {source_name}\n")
            process_job_file(full_path, OUTPUT_DIR, timestamp, source_name)
            archive_input_file(full_path, ARCHIVE_DIR, timestamp)

print(f"✅ Reports generated in: {OUTPUT_DIR}")
