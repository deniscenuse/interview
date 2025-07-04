import csv
import os

def prepare_report_files(output_dir, timestamp):
    """
    Create the 3 report CSV files with headers.
    """
    headers = ["level", "name", "pid", "start_time", "end_time", "duration", "source_file"]
    for level in ["warnings", "errors", "clean"]:
        path = os.path.join(output_dir, f"{timestamp}_{level}.csv")
        with open(path, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)

def write_report_line(level, name, pid, start, end, duration, source_file, output_dir, timestamp):
    """
    Append a line to the appropriate report file.
    """
    file_map = {
        "warning": "warnings",
        "error": "errors",
        "clean": "clean"
    }
    path = os.path.join(output_dir, f"{timestamp}_{file_map[level]}.csv")
    with open(path, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([level, name, pid, start, end, duration, source_file])

def write_no_files_found(level, output_dir, timestamp):
    """
    Write a line indicating no .log files found in input.
    The row is aligned with CSV headers.
    """
    file_map = {
        "warning": "warnings",
        "error": "errors",
        "clean": "clean"
    }
    path = os.path.join(output_dir, f"{timestamp}_{file_map[level]}.csv")
    with open(path, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["info", "No .log files found in input", "", "", "", "", ""])
