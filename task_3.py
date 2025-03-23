import sys
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional, Tuple

LOG_LEVELS = ["info", "debug", "warning", "error"]


def get_args() -> Tuple[str, Optional[str]]:

    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print(
            f"❌ Wrong format, use: python {sys.argv[0]} "
            "/path/to/logfile level(optional)"
        )
        sys.exit(1)

    file_path = sys.argv[1].strip()
    log_level = None
    if len(sys.argv) == 3:
        level_candidate = sys.argv[2].strip().lower()
        if level_candidate in LOG_LEVELS:
            log_level = level_candidate.upper()
        else:
            print(f"⚠️ Warning: Unknown log level '{level_candidate}', ignoring filter.")
    return file_path, log_level


def load_logs(file_path: str) -> List[str]:

    log_file = Path(file_path)
    if not log_file.exists() or not log_file.is_file():
        print("❌ Error: Log file not found")
        sys.exit(1)
    try:
        with log_file.open(mode="r", encoding="utf-8") as file:
            logs = [line.strip() for line in file if line.strip()]
        return logs
    except Exception as e:
        print(f"❌ Unexpected error while reading file: {e.args}")
        sys.exit(1)


def parse_log_line(line: str) -> Dict[str, str]:
    # Line example: "2024-01-22 08:30:01 INFO User logged in successfully."
    parts = line.split(" ", 3)
    if len(parts) < 4:
        return {}

    date, time, level, message = parts
    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message,
    }


def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[str]:
    filtred_logs = [
        f"{record.get('date')} {record.get('time')} - {record.get('message')}"
        for record in logs
        if record.get("level") == level
    ]

    return filtred_logs


def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    count = Counter(record["level"] for record in logs)
    return dict(count)


def display_log_counts(counts: Dict[str, int]) -> None:
    print(f"{'Рівень логування':<18} | Кількість")
    print("-" * 18 + "-|-" + "-" * 9)

    for level, count in counts.items():
        print(f"{level:<18} | {count}")


def main() -> None:
    file_path, log_level = get_args()
    raw_logs = load_logs(file_path=file_path)
    if not raw_logs:
        print("Записів не існує")
        sys.exit(0)

    logs = []
    for line in raw_logs:
        parsed = parse_log_line(line)
        if parsed:
            logs.append(parsed)
    counts = count_logs_by_level(logs=logs)

    display_log_counts(counts=counts)

    if log_level:
        print(f"Деталі логів для рівня '{log_level}':")
        for line in filter_logs_by_level(logs=logs, level=log_level):
            print(line)


if __name__ == "__main__":
    main()
