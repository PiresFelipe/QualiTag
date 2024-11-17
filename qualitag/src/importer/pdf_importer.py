from PyPDF2 import PdfReader

from ..questions import Answer
from .importer_base import ImporterBase


class PDFImporter(ImporterBase):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def import_data(self) -> Answer:
        """
        Imports data from a PDF file and returns it as an Answer object.
        This method reads the PDF file specified by the instance's filepath attribute,
        extracts text from each page, and concatenates it into a single string.
        Returns:
            Answer: An Answer object containing the extracted text from the PDF file.
        """
        
        text = ""
        with open(self.filepath, "rb") as f:
            reader = PdfReader(f)
            
            for page in reader.pages:
                text += page.extract_text()
            
        return Answer(text) 