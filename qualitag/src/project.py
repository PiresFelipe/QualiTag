import os
import pickle
from qualitag.src.questions import Question
from qualitag.src.tags import TagsManager
from qualitag.src.importer import import_data


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

    def add_question(self, text: str, answers_folder: str) -> None:

        question = Question(text)

        for file in os.listdir(answers_folder):
            try:
                answer = import_data(os.path.join(answers_folder, file))
                question.add_answer(answer)
            except ValueError:
                continue

        self.__questions.append(question)
