from itertools import count

from .answer import Answer


class Question:

    __id_counter = count()

    def __init__(self, question: str):
        self.__id = next(Question.__id_counter)
        self.question = question
        self.__answers: list[Answer] = []

    @property
    def id(self) -> int:
        return self.__id

    @property
    def answers(self) -> list[Answer]:
        return self.__answers

    def add_answer(self, answer: Answer):
        assert isinstance(answer, Answer), "answer must be an instance of Answer class"

        self.__answers.append(answer)

    def remove_answer(self, answer: Answer):
        assert isinstance(answer, Answer), "answer must be an instance of Answer class"

        self.__answers.remove(answer)
