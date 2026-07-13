from pathlib import Path


def ensure_directory(path: Path):

    path.mkdir(
        parents=True,
        exist_ok=True,
    )


def normalize_header(value):

    if value is None:
        return ""

    return str(value).strip()


def is_excel_file(path):

    return str(path).lower().endswith(".xlsx")
