from os.path import splitext

from .excel_importer import ExcelImporter
from .importer_base import ImporterBase
from .pdf_importer import PDFImporter


def import_data(filepath: str):
    _, ext = splitext(filepath)

    if ext == ".pdf":
        importer: ImporterBase = PDFImporter(filepath)
    else:
        raise ValueError(f"Unsupported file format: {ext}")

    return importer.import_data()


__all__ = ["import_data"]
