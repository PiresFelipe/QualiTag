from abc import ABC, abstractmethod
import pandas as pd


class ExporterBase(ABC):
    @abstractmethod
    def export(self, data):
        pass

    def as_dataframe(self, data) -> pd.DataFrame:
        return pd.DataFrame(data)
