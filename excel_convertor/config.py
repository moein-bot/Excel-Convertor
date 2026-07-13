"""
Project configuration.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

PACKAGE_DIR = PROJECT_ROOT / "excel_convertor"

MAPPING_DIR = PROJECT_ROOT / "mapping"

TEMPLATE_DIR = PROJECT_ROOT / "templates"

EXAMPLES_DIR = PROJECT_ROOT / "examples"

OUTPUT_DIR = PROJECT_ROOT / "output"

LOG_DIR = PROJECT_ROOT / "logs"

TESTS_DIR = PROJECT_ROOT / "tests"

DEFAULT_MAPPING_FILE = MAPPING_DIR / "default_mapping.yaml"

DEFAULT_OUTPUT_FILE = OUTPUT_DIR / "result.xlsx"

DEFAULT_LOG_FILE = LOG_DIR / "converter.log"

DEFAULT_USER_SHEET = "لیست بیمه شدگان"

DEFAULT_GUIDE_SHEET = "راهنمای فایل اکسل عمر و حوادث"

DEFAULT_TEMPLATE_SHEET = "Sheet1"

HEADER_ROW = 1

FIRST_DATA_ROW = 2

SUPPORTED_EXTENSIONS = {".xlsx"}

APPLICATION_NAME = "Excel Convertor"

APPLICATION_VERSION = "0.1.0"
