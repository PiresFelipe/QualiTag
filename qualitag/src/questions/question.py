from itertools import count

from .answer import Answer


class Question:
    """
    A class to represent a question.
    Attributes
    ----------
    question : str
        The text of the question.
    id : int
        The unique identifier for the question.
    answers : list[Answer]
        A list of answers associated with the question.
    Methods
    -------
    add_answer(answer: Answer):
        Adds an answer to the question.
    remove_answer(answer: Answer):
        Removes an answer from the question.
    """

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
        """
        Adds an answer to the question.
        Args:
            answer (Answer): The answer to be added. Must be an instance of the Answer class.
        Raises:
            AssertionError: If the provided answer is not an instance of the Answer class.
        """
        assert isinstance(answer, Answer), "answer must be an instance of Answer class"

        self.__answers.append(answer)

    def remove_answer(self, answer: Answer):
        """
        Removes the specified answer from the list of answers.
        Args:
            answer (Answer): The answer to be removed. Must be an instance of the Answer class.
        Raises:
            AssertionError: If the provided answer is not an instance of the Answer class.
        """
        
        assert isinstance(answer, Answer), "answer must be an instance of Answer class"

        self.__answers.remove(answer)
