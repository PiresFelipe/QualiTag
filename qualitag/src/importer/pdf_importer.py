from PyPDF2 import PdfReader

from .importer_base import ImporterBase
from ..questions import Answer


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