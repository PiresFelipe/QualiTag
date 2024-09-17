from os.path import splitext

from qualitag.src.exporter.exporter_base import ExporterBase
from .json_exporter import JSONExporter
from .xlsx_exporter import ExcelExporter
from .pdf_exporter import PDFExporter

def export(project, filepath: str):
    _, ext = splitext(filepath)

    if ext == ".json":
        exporter: ExporterBase = JSONExporter(filepath)
    elif ext == ".xlsx":
        exporter = ExcelExporter(filepath)
    elif ext == ".pdf":
        exporter = PDFExporter(filepath)
    else:
        raise ValueError("Invalid file extension")

    exporter.export(project)


__all__ = ["export"]
