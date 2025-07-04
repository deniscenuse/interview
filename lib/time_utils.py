from datetime import datetime


def get_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def convert_to_seconds(time_str):
    """Convert HH:MM:SS to seconds."""
    h, m, s = map(int, time_str.strip().split(":"))
    return h * 3600 + m * 60 + s


def format_duration(seconds):
    """Convert seconds to HH:MM:SS."""
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02}:{m:02}:{s:02}"


def handle_day_wraparound(start_sec, end_sec):
    """Handle cases when end time is after midnight."""
    if end_sec < start_sec:
        end_sec += 86400  # add 24h in seconds
    return end_sec
