"""
Application configuration.

This module contains project-wide paths and default settings.
Every other module should import configuration values from here
instead of hardcoding paths or filenames.
"""

from pathlib import Path

# ============================================================================
# Project Directories
# ============================================================================

# excel-convertor/
PROJECT_ROOT = Path(__file__).resolve().parent.parent

PACKAGE_DIR = PROJECT_ROOT / "excel_convertor"

MAPPING_DIR = PROJECT_ROOT / "mapping"

TEMPLATE_DIR = PROJECT_ROOT / "templates"

EXAMPLES_DIR = PROJECT_ROOT / "examples"

OUTPUT_DIR = PROJECT_ROOT / "output"

LOG_DIR = PROJECT_ROOT / "logs"

TESTS_DIR = PROJECT_ROOT / "tests"

# ============================================================================
# Default Files
# ============================================================================

DEFAULT_MAPPING_FILE = MAPPING_DIR / "default_mapping.yaml"

DEFAULT_OUTPUT_FILE = OUTPUT_DIR / "result.xlsx"

DEFAULT_LOG_FILE = LOG_DIR / "converter.log"

# ============================================================================
# Excel Configuration
# ============================================================================

DEFAULT_USER_SHEET = "لیست بیمه شدگان"

DEFAULT_CODE_SHEET = "لیست کدها"

DEFAULT_TEMPLATE_SHEET = "Sheet1"

HEADER_ROW = 1

FIRST_DATA_ROW = 2

# ============================================================================
# Supported Formats
# ============================================================================

SUPPORTED_EXTENSIONS = {
    ".xlsx",
}

# ============================================================================
# Logging
# ============================================================================

LOG_LEVEL = "INFO"

LOG_FORMAT = (
    "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
)

# ============================================================================
# Application
# ============================================================================

APPLICATION_NAME = "Excel Convertor"

APPLICATION_VERSION = "0.1.0"

AUTHOR = "Moein Khazaee"

LICENSE = "MIT"
