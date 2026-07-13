from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

MAPPING_DIR = ROOT_DIR / "mapping"

TEMPLATE_DIR = ROOT_DIR / "templates"

OUTPUT_DIR = ROOT_DIR / "output"

LOG_DIR = ROOT_DIR / "logs"

DEFAULT_MAPPING_FILE = MAPPING_DIR / "default_mapping.yaml"

DEFAULT_OUTPUT_NAME = "result.xlsx"

LOG_FILE = LOG_DIR / "converter.log"

SUPPORTED_EXTENSIONS = (
    ".xlsx",
)
