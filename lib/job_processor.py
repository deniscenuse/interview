import os
from collections import defaultdict
from lib.time_utils import convert_to_seconds, handle_day_wraparound, format_duration
from lib.report_writer import write_report_line


def process_job_file(input_file, output_dir, timestamp, source_name):
    start_times = {}
    job_names = {}

    with open(input_file, 'r') as f:
        for line in f:
            parts = [p.strip() for p in line.strip().split(",")]
            if len(parts) != 4:
                continue  # skip invalid lines

            time_str, name, event, pid = parts
            key = f"{name}_{pid}"

            if event == "START":
                start_times[key] = time_str
                job_names[key] = name

            elif event == "END":
                if key not in start_times:
                    continue  # END without START

                start_time = start_times[key]
                start_sec = convert_to_seconds(start_time)
                end_sec = convert_to_seconds(time_str)
                end_sec = handle_day_wraparound(start_sec, end_sec)
                duration = end_sec - start_sec
                duration_fmt = format_duration(duration)

                if duration > 600:
                    write_report_line("error", name, pid, start_time, time_str, duration_fmt, source_name, output_dir, timestamp)
                elif duration > 300:
                    write_report_line("warning", name, pid, start_time, time_str, duration_fmt, source_name, output_dir, timestamp)
                else:
                    write_report_line("clean", name, pid, start_time, time_str, duration_fmt, source_name, output_dir, timestamp)

                # Cleanup
                del start_times[key]
                del job_names[key]
