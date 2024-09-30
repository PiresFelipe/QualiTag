from os.path import splitext

from qualitag.src.exporter.exporter_base import ExporterBase

from .pdf_exporter import PDFExporter
from .xlsx_exporter import ExcelExporter


def export(project, filepath: str): # pragma: no cover
    _, ext = splitext(filepath)

    if ext == ".xlsx":
        exporter: ExporterBase = ExcelExporter(filepath)
    elif ext == ".pdf":
        exporter: ExporterBase = PDFExporter(filepath)
    else:
        raise ValueError("Invalid file extension")

    exporter.export(project)


__all__ = ["export"]
