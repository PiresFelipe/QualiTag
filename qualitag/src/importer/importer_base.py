from abc import ABC, abstractmethod


class ImporterBase(ABC): # pragma: no cover
    @abstractmethod
    def import_data(self):
        pass
