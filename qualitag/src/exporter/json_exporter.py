from json import dump

from .exporter_base import ExporterBase


class JSONExporter(ExporterBase):
    
    def __init__(self, filepath: str) -> None:
        self.filepath =  filepath
        
    def export(self, data):
        with open(self.filepath, "w") as f:
            dump(data, f)
