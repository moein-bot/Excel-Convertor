from pathlib import Path

from openpyxl import load_workbook

from .config import (
    DEFAULT_TEMPLATE_SHEET,
    DEFAULT_USER_SHEET,
)

from .logger import get_logger

logger = get_logger(__name__)


class IOHandler:

    def __init__(self, template_path, user_path):

        self.template_path = Path(template_path)

        self.user_path = Path(user_path)

        self.template_workbook = None

        self.user_workbook = None

    def load(self):

        logger.info("Loading template workbook...")

        self.template_workbook = load_workbook(
            self.template_path
        )

        logger.info("Loading user workbook...")

        self.user_workbook = load_workbook(
            self.user_path,
            data_only=True,
        )

    def template_sheet(self):

        return self.template_workbook[
            DEFAULT_TEMPLATE_SHEET
        ]

    def user_sheet(self):

        return self.user_workbook[
            DEFAULT_USER_SHEET
        ]

    def headers(self, sheet):

        result = {}

        for cell in sheet[1]:

            if cell.value is None:
                continue

            result[str(cell.value).strip()] = cell.column

        return result

    def rows(self, sheet):

        headers = [
            cell.value
            for cell in sheet[1]
        ]

        data = []

        for row in sheet.iter_rows(
            min_row=2,
            values_only=True,
        ):

            if all(v is None for v in row):
                continue

            item = {}

            for h, v in zip(headers, row):

                item[str(h).strip()] = v

            data.append(item)

        return data

    def write(
        self,
        sheet,
        row,
        column,
        value,
    ):

        sheet.cell(
            row=row,
            column=column,
        ).value = value

    def save(self, output_path):

        logger.info(
            f"Saving workbook to {output_path}"
        )

        self.template_workbook.save(output_path)
