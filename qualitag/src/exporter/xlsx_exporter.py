import pandas as pd

from .exporter_base import ExporterBase


class ExcelExporter(ExporterBase): # pragma: no cover

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def export(self, project):
        writer = pd.ExcelWriter(self.filepath, engine="openpyxl")
        for i, question in enumerate(project.questions):
            data = {
                "answer": [],
                "tag": [],
                "text": [],
            }
            for j, answer in enumerate(question.answers):
                for tag, texts in answer.get_all_tags(as_text=True).items():
                    for text in texts:
                        data["answer"].append(j)
                        data["tag"].append(tag)
                        data["text"].append(text)
            df = pd.DataFrame(data)
            df.to_excel(writer, index=False, sheet_name=f"Q{i+1:03d}")
        writer.close()
