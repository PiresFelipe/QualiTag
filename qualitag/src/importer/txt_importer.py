from .importer_base import ImporterBase
from ..questions import Answer

class TXTImporter(ImporterBase):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def import_data(self):
        text = ""
        with open(self.filepath, "r", encoding="utf-8") as f:
            text = f.read()
        return Answer(text)
