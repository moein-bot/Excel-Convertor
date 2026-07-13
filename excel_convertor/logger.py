import logging

from .config import LOG_DIR, DEFAULT_LOG_FILE

LOG_DIR.mkdir(parents=True, exist_ok=True)


def get_logger(name: str):

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        DEFAULT_LOG_FILE,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
