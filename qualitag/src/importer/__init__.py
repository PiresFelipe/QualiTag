from os.path import splitext
from .importer_base import ImporterBase
from .excel_importer import ExcelImporter


def import_data(filepath: str):
    _, ext = splitext(filepath)

    if ext == ".xlsx":
        importer: ImporterBase = ExcelImporter(filepath)
    else:
        raise ValueError(f"Unsupported file format: {ext}")

    return importer.import_data()


__all__ = ["import_data"]
