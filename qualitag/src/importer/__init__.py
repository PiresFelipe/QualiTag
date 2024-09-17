from os.path import splitext

from .importer_base import ImporterBase
from .pdf_importer import PDFImporter
from .txt_importer import TXTImporter


def import_data(filepath: str):
    _, ext = splitext(filepath)

    if ext == ".pdf":
        importer: ImporterBase = PDFImporter(filepath)
    elif ext == ".txt":
        importer: ImporterBase = TXTImporter(filepath)
    else:
        raise ValueError(f"Unsupported file format: {ext}")

    return importer.import_data()


__all__ = ["import_data"]
