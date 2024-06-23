from abc import ABC, abstractmethod


class ImporterBase(ABC):
    @abstractmethod
    def import_data(self):
        pass
