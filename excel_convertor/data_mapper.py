"""
data_mapper.py

Maps user workbook rows to the destination template.

Current implementation follows the agreed mapping:

نام                    -> Name
نام خانوادگی           -> LName
شماره شناسنامه         -> IdentityNo
تاریخ تولد             -> BirthYear/BirthMonth/BirthDay
کد ملی                 -> CodeMelli
جنسیت                  -> Jens
کد وضعیت تأهل          -> tahol
"""

from __future__ import annotations

from typing import Dict, Any

from .constants import (
    GENDER_MAP,
    MARITAL_MAP,
)

from .utils import split_persian_date


class MappingError(Exception):
    """Raised when mapping cannot be completed."""


class DataMapper:

    def __init__(self):
        self.column_mapping = {
            "نام": "Name",
            "نام خانوادگی": "LName",
            "شماره شناسنامه": "IdentityNo",
            "کد ملی": "CodeMelli",
        }

    # -------------------------------------------------------------

    def map_row(self, row: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert one user row into destination row.
        """

        output = {}

        # --------------------------
        # Direct Mapping
        # --------------------------

        for source, destination in self.column_mapping.items():
            output[destination] = row.get(source)

        # --------------------------
        # Birth Date
        # --------------------------

        year, month, day = split_persian_date(
            row["تاریخ تولد"]
        )

        output["BirthYear"] = year
        output["BirthMonth"] = month
        output["BirthDay"] = day

        # --------------------------
        # Gender
        # --------------------------

        gender = int(row["جنسیت"])

        output["Jens"] = GENDER_MAP[gender]

        # --------------------------
        # Marital Status
        # --------------------------

        marital = int(row["کد وضعیت تأهل"])

        output["tahol"] = MARITAL_MAP[marital]

        return output

    # -------------------------------------------------------------

    def map_rows(self, rows):
        """
        Convert all rows.
        """

        results = []

        for row in rows:
            results.append(
                self.map_row(row)
            )

        return results

    # -------------------------------------------------------------

    @staticmethod
    def destination_columns():
        """
        Destination columns used by template.
        """

        return [
            "Name",
            "LName",
            "IdentityNo",
            "BirthYear",
            "BirthMonth",
            "BirthDay",
            "CodeMelli",
            "Jens",
            "tahol",
        ]
