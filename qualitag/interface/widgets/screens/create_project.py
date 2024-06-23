import os
from typing import Any
import customtkinter as ctk
from tkinter import filedialog

from qualitag import Answer, import_data, Question


class CreateProjectScreen(ctk.CTkFrame):

    def __init__(self, *args, question: Question, command: Any, **kwargs):
        super().__init__(*args, **kwargs)

        title = ctk.CTkFont("Arial black", 20, "bold")
        subtitle = ctk.CTkFont("Arial", 20)

        ctk.CTkLabel(self, text="Bem-vindo ao QualiTag!", font=title).pack(pady=20)

        ctk.CTkLabel(
            self,
            text="Para começar, inicialmente escreva a pergunta que gerou as respostas\ne importe os arquivos PDF que deseja analisar",
            font=subtitle,
        ).pack(pady=[0, 10])

        self.question = ctk.CTkEntry(
            self, font=subtitle, placeholder_text="Digite a pergunta aqui"
        )
        self.question.pack(fill="x", padx=100)

        ctk.CTkButton(self, text="Import data", command=self.__import_data).place(
            relx=0.5, rely=0.5, anchor="center"
        )

        self.__data = []
        self.__question = question
        self.__command = command

        self.__start = ctk.CTkButton(
            self,
            text="codificar!",
            command=self.start_code,
            state="disabled",
            hover=False,
            fg_color="#C0C0C0",
            text_color_disabled="#36454F",
        )
        self.__start.pack(pady=20, side="bottom")

    def __import_data(self) -> list[Answer]:
        data = []
        folder = filedialog.askdirectory(initialdir=".")
        print(folder)
        for file in os.listdir(folder):
            if file.endswith(".pdf"):
                data.append(import_data(os.path.join(folder, file)))

        self.__data = data
        if len(data) > 0:
            self.__start.configure(state="normal", fg_color="#6082B6")
        return data

    def start_code(self):

        self.__question.question = self.question.get()
        for answer in self.__data:
            self.__question.add_answer(answer)

        self.destroy()

        if self.__command is not None:
            self.__command()
