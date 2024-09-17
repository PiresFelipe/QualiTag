from PyPDF2 import PdfReader

from ..questions import Answer
from .importer_base import ImporterBase


class PDFImporter(ImporterBase):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def import_data(self) -> Answer:
        text = ""
        with open(self.filepath, "rb") as f:
            reader = PdfReader(f)
            
            for page in reader.pages:
                text += page.extract_text()
            
        return Answer(text)