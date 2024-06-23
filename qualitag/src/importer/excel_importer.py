from .importer_base import ImporterBase


class ExcelImporter(ImporterBase):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def import_data(self):
        pass
