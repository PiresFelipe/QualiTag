from PyPDF2 import PdfFileReader

from .importer_base import ImporterBase
from ..questions import Answer


class PDFImporter(ImporterBase):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def import_data(self) -> Answer:
        text = ""
        with open(self.filepath, "rb") as f:
            reader = PdfFileReader(f)
            
            for page in range(reader.getNumPages()):
                text += reader.getPage(page).extract_text()
            
        return Answer(text)