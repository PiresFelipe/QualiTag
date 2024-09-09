import customtkinter as ctk
from tkinter import IntVar
from qualitag.src import Question


class QuestionsSelector(ctk.CTkOptionMenu):

    def __init__(self, *args, questions: list[Question], **kwargs):
        super().__init__(*args, **kwargs)

        self.__selected = IntVar()
        self.__questions = questions

        self._command = self.__select
        self.set("")
        self.update_questions()

    @property
    def selected(self) -> IntVar:
        return self.__selected

    def __select(self, value: str):
        _, num = value.split(" ")
        self.__selected.set(int(num))

    def select(self, question_idx: int):
        _value = f"Questão {question_idx:03d}"
        if _value in self.cget("values"):
            self.set(_value)

    def update_questions(self):
        questions = []
        for i in range(len(self.__questions)):
            _value = f"Questão {i+1:03d}"
            questions.append(_value)
        self.configure(values=questions)
        if len(questions) <= 0:
            self.configure(state="disabled")
        else:
            self.configure(state="normal")
