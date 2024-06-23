import os

from qualitag.src.exporter.exporter_base import ExporterBase
from .json_exporter import JSONExporter
from .xlsx_exporter import ExcelExporter

def export(data, filepath: str):
    file, ext = os.path.splitext(filepath)

    if ext == ".json":
        exporter: ExporterBase = JSONExporter(filepath)
    elif ext == ".xlsx":
        exporter = ExcelExporter(filepath)
    else:
        raise ValueError("Invalid file extension")

    exporter.export(data)


__all__ = ["export", "JSONExporter"]
