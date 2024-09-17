import customtkinter as ctk

from qualitag.src import Question

from ...utils import fonts
from .coding_box import CodingBox


class AnswerSelector(ctk.CTkFrame):

    def __init__(self, *args, question: Question, tags_mng, events, **kwargs):
        super().__init__(*args, **kwargs)

        self.__question = question
        self.__current = None
        self.__values = [
            f"Resposta {i:03d}" for i in range(1, len(self.__question.answers) + 1)
        ]

        self.__codes_boxes = [
            CodingBox(
                self,
                tags_manager=tags_mng,
                events=events,
                answer=answer,
                font=("Roboto", 16),
            )
            for answer in self.__question.answers
        ]

        ctk.CTkLabel(
            self,
            text="Selecione a resposta que deseja codificar:",
            font=ctk.CTkFont(**fonts["h3"]),
        ).pack(anchor="w", padx=10)
        ctk.CTkOptionMenu(
            self,
            values=self.__values,
            command=self.on_change_sel,
        ).pack(anchor="w", padx=10)

        if len(self.__codes_boxes) > 0:
            self.on_change_sel(self.__values[0])

    def on_change_sel(self, value):
        index = self.__values.index(value)
        new = self.__codes_boxes[index]

        if new != self.__current:
            if self.__current is not None:
                self.__current.pack_forget()
            new.pack(fill="both", expand=True, pady=10, padx=10)
            self.__current = new
