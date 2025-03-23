import sys
from pathlib import Path

LOG_LEVELS = ["info", "debug", "warning", "error"]


def parse_log_line(line: str) -> dict:
    return {}


def load_logs(file_path: str) -> list:
    return []


def filter_logs_by_level(logs: list, level: str) -> list:
    return []


def count_logs_by_lebel(logs: list) -> dict:
    return {}


def display_log_counts(counts: dict) -> None:
    return None


def main() -> None:

    if len(sys.argv) < 2:
        print("❌ Error: No path provided")
        sys.exit(1)

    path = sys.argv[1]
    log_file = Path(path.strip())
    if not log_file.exists() or not log_file.is_file():
        print("❌ Error: Log file not found")
        sys.exit(1)
    log_level = (
        sys.argv[2]
        if len(sys.argv) == 3 and sys.argv[2].strip().lower() in LOG_LEVELS
        else None
    )
    print(f"{log_file}   {log_level}")


if __name__ == "__main__":
    main()
