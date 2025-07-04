import csv
import os


def prepare_report_files(output_dir, timestamp):
    os.makedirs(output_dir, exist_ok=True)
    headers = ["level", "name", "pid", "start_time", "end_time", "duration", "source_file"]
    for level in ["warnings", "errors", "clean"]:
        path = os.path.join(output_dir, f"{timestamp}_{level}.csv")
        with open(path, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)


def write_report_line(level, name, pid, start, end, duration, source_file, output_dir, timestamp):
    file_map = {
        "warning": "warnings",
        "error": "errors",
        "clean": "clean"
    }
    level_key = file_map.get(level)
    if not level_key:
        return  # unknown level, skip

    path = os.path.join(output_dir, f"{timestamp}_{level_key}.csv")
    with open(path, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([level, name, pid, start, end, duration, source_file])
