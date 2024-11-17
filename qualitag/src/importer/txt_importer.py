from .importer_base import ImporterBase
from ..questions import Answer

class TXTImporter(ImporterBase):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def import_data(self):
        """
        Imports data from a text file specified by the filepath attribute.
        Reads the contents of the file using UTF-8 encoding and returns an Answer object
        containing the text.
        Returns:
            Answer: An Answer object containing the text read from the file.
        """
        
        text = ""
        with open(self.filepath, "r", encoding="utf-8") as f:
            text = f.read()
        return Answer(text)
