from pathlib import Path


def normalize(value):

    if value is None:
        return ""

    return str(value).strip()


def ensure_directory(path: Path):

    path.mkdir(
        parents=True,
        exist_ok=True,
    )


def is_excel(path: Path):

    return path.suffix.lower() == ".xlsx"


def split_persian_date(date_string):

    if date_string is None:
        return "", "", ""

    date_string = str(date_string)

    if "/" in date_string:
        year, month, day = date_string.split("/")

    elif "-" in date_string:
        year, month, day = date_string.split("-")

    else:
        raise ValueError(
            f"Invalid Persian date: {date_string}"
        )

    return (
        int(year),
        int(month),
        int(day),
    )
