from .exporter_base import ExporterBase

class ExcelExporter(ExporterBase):

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def export(self, data):
        df = {"tag": [], "answer": []}
        for tag in data:
            for answer in data[tag]:
                df["tag"].append(tag)
                df["answer"].append(answer)
        df = self.as_dataframe(df)
        df.to_excel(self.filepath, index=False, sheet_name="Answers")
