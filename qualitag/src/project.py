import os
import pickle
from qualitag.src.questions import Question
from qualitag.src.tags import TagsManager
from qualitag.src.importer import import_data
from qualitag.src.reports import ChartReport
from PIL import Image


class CodingProject:

    def __init__(self) -> None:

        self.__questions: list[Question] = []
        self.__tags_manager = TagsManager()
        self.__chart_generator = ChartReport()

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

    def generate_wordcloud(self, tag: str, **kwargs) -> Image.Image:
        text = ""

        for question in self.__questions:
            for answer in question.answers:
                text += " ".join(answer.get_tag_text(tag))
            text += " "

        if len(text) < 5:
            raise ValueError(f"Insufficient values for tag '{tag}'")

        return self.__chart_generator.wordcloud(text, **kwargs).to_image()

    def generate_most_common_tags_chart(self, **kwargs) -> Image.Image:
        tags_count = self.__tags_manager.counter
        return self.__chart_generator.most_common_tags(tags_count, **kwargs)
