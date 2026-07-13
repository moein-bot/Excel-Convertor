"""
cli.py

Command-line interface for Excel Convertor.
"""

import argparse
import sys
from pathlib import Path

from .converter import convert


def build_parser():
    parser = argparse.ArgumentParser(
        prog="excel-convertor",
        description="Convert a user Excel workbook into the template workbook."
    )

    parser.add_argument(
        "--template",
        required=True,
        help="Path to template Excel file (.xlsx)"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to user Excel file (.xlsx)"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Output Excel file (.xlsx)"
    )

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    try:
        output = convert(
            template_path=Path(args.template),
            user_path=Path(args.input),
            output_path=Path(args.output),
        )

        print(f"Conversion completed successfully.\nOutput: {output}")
        return 0

    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
