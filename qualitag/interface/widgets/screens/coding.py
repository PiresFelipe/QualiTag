import os
from tkinter import filedialog
import customtkinter as ctk

from qualitag.src import Question, export
from ..shared.coding_box import CodingBox
from ..tags.tags_list import TagsList


class CodingScreen(ctk.CTkFrame):

    def __init__(self, *args, question: Question, tags_mng, events, **kwargs):
        super().__init__(*args, **kwargs)

        self.__manager = tags_mng
        self.__events = events
        self.__question = question
        self.__values = [
            f"Resposta {i:03d}" for i in range(1, len(self.__question.answers) + 1)
        ]

        self.__main_container = ctk.CTkFrame(self)
        self.__lateral_container = ctk.CTkFrame(self)

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)

        self.__main_container.grid(row=0, column=0, sticky="nsew")
        self.__lateral_container.grid(row=0, column=1, sticky="nsew")

        self.__codes_boxes = [
            CodingBox(
                self.__main_container,
                tags_manager=tags_mng,
                events=events,
                answer=answer,
                font=("Roboto", 16),
            )
            for answer in self.__question.answers
        ]

        self.__current_answer = None
        self.__build()

    def __build(self):

        font = ctk.CTkFont("Roboto", 30, "bold")

        ctk.CTkLabel(
            self.__main_container,
            text="QUESTÃO 01",
            font=font,
            justify="left",
            anchor="w",
        ).pack(pady=[20, 10], padx=10, fill="x")

        font = ctk.CTkFont("Roboto", 20, slant="italic")
        ctk.CTkLabel(
            self.__main_container,
            text=self.__question.question,
            font=font,
            justify="left",
            anchor="w",
        ).pack(pady=10, padx=10, fill="x")

        font = ctk.CTkFont("Roboto", 16)
        self.__options_menu = ctk.CTkOptionMenu(
            self.__main_container,
            values=self.__values,
            font=font,
            command=self.__selected_answer,
        )
        self.__options_menu.pack(pady=10, padx=10, fill="x")

        self.__current_answer = self.__codes_boxes[0]
        self.__current_answer.pack(fill="both", expand=True, pady=10, padx=10)

        TagsList(
            self.__lateral_container,
            manager=self.__manager,
            events=self.__events,
            height=440,
        ).pack(fill="both", expand=True, pady=10, padx=10)

        ctk.CTkButton(
            self.__lateral_container,
            text="Criar Tag",
            command=self.master.open_tag_creator,
        ).pack(fill="x", padx=10, pady=10)

        ctk.CTkButton(
            self.__lateral_container,
            text="Exportar codificação >",
            fg_color="#E34234",
            hover_color="#BD271A",
            command=self.__export_coding,
        ).pack(fill="x", padx=10, pady=[0, 10])

    def __selected_answer(self, value):
        index = self.__values.index(value)
        new = self.__codes_boxes[index]

        if new != self.__current_answer:
            self.__current_answer.pack_forget()
            new.pack(fill="both", expand=True, pady=10, padx=10)
            self.__current_answer = new

    def __export_coding(self):

        file = filedialog.asksaveasfilename(
            title="Exportar codificação",
            initialdir=os.getcwd(),
            filetypes=[("Excel files", "*.xlsx")],
            defaultextension=".xlsx",
        )

        data = {
            "question": [],
            "answer": [],
            "codes": [],
            "text": [],
        }

        for i, answer in enumerate(self.__question.answers):
            tags = answer.get_all_tags(as_text=True)
            for tag in tags:
                data["question"].extend([self.__question.id] * len(tags[tag]))
                data["answer"].extend([i] * len(tags[tag]))
                data["codes"].extend([tag] * len(tags[tag]))
                data["text"].extend(tags[tag])

        export(data, file)
