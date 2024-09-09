import pickle
from qualitag.src.questions import Question
from qualitag.src.tags import TagsManager


class CodingProject:

    def __init__(self) -> None:

        self.__questions: list[Question] = []
        self.__tags_manager = TagsManager()

    @property
    def questions(self) -> list[Question]:
        return self.__questions

    @property
    def tags_manager(self) -> TagsManager:
        return self.__tags_manager

    @staticmethod
    def load(filename: str) -> "CodingProject":
        with open(filename, "rb") as file:
            return pickle.load(file)

    def save(self, filename: str) -> None:
        with open(filename, "wb") as file:
            pickle.dump(self, file)
