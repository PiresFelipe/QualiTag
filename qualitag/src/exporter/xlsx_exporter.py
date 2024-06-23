from .exporter_base import ExporterBase

class ExcelExporter(ExporterBase):

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def export(self, data):
        df = self.as_dataframe(data)
        df.to_excel(self.filepath, index=False, sheet_name="Answers")
