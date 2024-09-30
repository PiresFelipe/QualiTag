from abc import ABC, abstractmethod

import pandas as pd


class ExporterBase(ABC): # pragma: no cover
    @abstractmethod
    def export(self, data):
        pass

    def as_dataframe(self, data) -> pd.DataFrame:
        return pd.DataFrame(data)
