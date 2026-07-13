"""
validator.py

Validation layer for Excel Convertor.

Responsible for:

- Checking required worksheets
- Checking required columns
- Validating user data
- Raising descriptive errors before conversion starts
"""

from __future__ import annotations

import re
from typing import Dict, List

from .constants import (
    GENDER_MAP,
    MARITAL_MAP,
)


class ValidationError(Exception):
    """Base validation exception."""


class MissingColumnError(ValidationError):
    """Raised when a required column does not exist."""


class InvalidValueError(ValidationError):
    """Raised when a cell contains an invalid value."""


class Validator:

    REQUIRED_COLUMNS = [
        "نام",
        "نام خانوادگی",
        "شماره شناسنامه",
        "تاریخ تولد",
        "کد ملی",
        "جنسیت",
        "کد وضعیت تأهل",
    ]

    DATE_PATTERN = re.compile(r"^\d{4}[/-]\d{1,2}[/-]\d{1,2}$")

    NATIONAL_ID_PATTERN = re.compile(r"^\d{10}$")

    # -------------------------------------------------------------

    @classmethod
    def validate_headers(cls, headers: Dict[str, int]) -> None:
        """
        Validate required headers.
        """

        missing = []

        for column in cls.REQUIRED_COLUMNS:
            if column not in headers:
                missing.append(column)

        if missing:
            raise MissingColumnError(
                f"Missing required columns: {', '.join(missing)}"
            )

    # -------------------------------------------------------------

    @classmethod
    def validate_rows(cls, rows: List[dict]) -> None:
        """
        Validate all rows.
        """

        for index, row in enumerate(rows, start=2):
            cls.validate_row(row, index)

    # -------------------------------------------------------------

    @classmethod
    def validate_row(cls, row: dict, row_number: int) -> None:

        cls.validate_required(row, row_number)

        cls.validate_birth(row, row_number)

        cls.validate_gender(row, row_number)

        cls.validate_marital(row, row_number)

        cls.validate_national_code(row, row_number)

    # -------------------------------------------------------------

    @staticmethod
    def validate_required(row: dict, row_number: int):

        required = [
            "نام",
            "نام خانوادگی",
            "شماره شناسنامه",
            "تاریخ تولد",
            "کد ملی",
            "جنسیت",
            "کد وضعیت تأهل",
        ]

        for field in required:

            value = row.get(field)

            if value is None:
                raise InvalidValueError(
                    f"Row {row_number}: '{field}' is empty."
                )

            if str(value).strip() == "":
                raise InvalidValueError(
                    f"Row {row_number}: '{field}' is empty."
                )

    # -------------------------------------------------------------

    @classmethod
    def validate_birth(cls, row, row_number):

        birth = str(row["تاریخ تولد"]).strip()

        if not cls.DATE_PATTERN.match(birth):

            raise InvalidValueError(
                f"Row {row_number}: Invalid birth date '{birth}'."
            )

        parts = re.split(r"[/-]", birth)

        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])

        if year < 1200 or year > 1600:

            raise InvalidValueError(
                f"Row {row_number}: Invalid birth year."
            )

        if month < 1 or month > 12:

            raise InvalidValueError(
                f"Row {row_number}: Invalid birth month."
            )

        if day < 1 or day > 31:

            raise InvalidValueError(
                f"Row {row_number}: Invalid birth day."
            )

    # -------------------------------------------------------------

    @classmethod
    def validate_gender(cls, row, row_number):

        try:
            gender = int(row["جنسیت"])
        except Exception:
            raise InvalidValueError(
                f"Row {row_number}: Invalid gender."
            )

        if gender not in GENDER_MAP:

            raise InvalidValueError(
                f"Row {row_number}: Unknown gender code '{gender}'."
            )

    # -------------------------------------------------------------

    @classmethod
    def validate_marital(cls, row, row_number):

        try:
            status = int(row["کد وضعیت تأهل"])
        except Exception:

            raise InvalidValueError(
                f"Row {row_number}: Invalid marital status."
            )

        if status not in MARITAL_MAP:

            raise InvalidValueError(
                f"Row {row_number}: Unknown marital status '{status}'."
            )

    # -------------------------------------------------------------

    @classmethod
    def validate_national_code(cls, row, row_number):

        code = str(row["کد ملی"]).strip()

        if not cls.NATIONAL_ID_PATTERN.match(code):

            raise InvalidValueError(
                f"Row {row_number}: Invalid national code '{code}'."
            )

    # -------------------------------------------------------------

    @staticmethod
    def validate_sheet_exists(workbook, sheet_name):

        if sheet_name not in workbook.sheetnames:

            raise ValidationError(
                f"Worksheet '{sheet_name}' not found."
            )

    # -------------------------------------------------------------

    @staticmethod
    def validate_not_empty(rows):

        if len(rows) == 0:

            raise ValidationError(
                "Worksheet contains no data."
            )

    # -------------------------------------------------------------

    @classmethod
    def validate(cls, headers, rows):
        """
        Complete validation pipeline.
        """

        cls.validate_headers(headers)

        cls.validate_not_empty(rows)

        cls.validate_rows(rows)

        return True
