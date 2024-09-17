import os
from tkinter import StringVar, filedialog, messagebox

import customtkinter as ctk

from qualitag.src import CodingProject

from ...utils import fonts


class QuestionCreator(ctk.CTkToplevel):

    def __init__(self, *args, project: CodingProject, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Create a new Question")

        self.__folder = StringVar()
        self.__text = StringVar()
        self.__folder.trace_add(mode="write", callback=self.check_folder)
        self.__project = project

        ctk.CTkLabel(
            self, text="Qual foi a pergunta realizada?", font=ctk.CTkFont(**fonts["h2"])
        ).pack(fill="x", anchor="w", padx=10)
        ctk.CTkEntry(
            self, textvariable=self.__text, font=ctk.CTkFont(**fonts["body"])
        ).pack(fill="x", padx=10)

        ctk.CTkLabel(self, text="Selecione a pasta com as respostas").pack(
            fill="x", anchor="w", padx=10
        )
        ctk.CTkLabel(
            self,
            text="* lembre-se que as repostas devem estar em formato PDF ou txt e em arquivos separados",
            font=ctk.CTkFont(**fonts["small"]),
        ).pack(fill="x")

        line = ctk.CTkFrame(self)
        line.pack(fill="x", padx=10)

        ctk.CTkButton(
            line,
            text="Selecionar pasta",
            command=lambda: self.__folder.set(filedialog.askdirectory(mustexist=True)),
        ).pack(side="left")
        ctk.CTkEntry(
            line,
            state="disabled",
            textvariable=self.__folder,
            fg_color="transparent",
            border_width=0,
        ).pack(fill="x", padx=10)

        self.__error_label = ctk.CTkLabel(self, text="", text_color="red", font=ctk.CTkFont(**fonts["h3"]))
        self.__error_label.pack(fill="x", pady=10)

        self.__btn = ctk.CTkButton(
            self, text="Criar", state="disabled", command=self.on_create
        )
        self.__btn.pack(pady=10)

    def check_folder(self, *args):
        if not self.valid_folder():
            self.__error_label.configure(
                text="A pasta selecionada não contém arquivos PDF ou txt"
            )
            self.__btn.configure(state="disabled")
        else:
            self.__error_label.configure(text="")
            self.__btn.configure(state="normal")

    def valid_folder(self) -> bool:

        for file in os.listdir(self.__folder.get()):
            if file.endswith((".pdf", ".txt")):
                return True
        return False

    def on_create(self):
        try:
            self.__project.add_question(
                self.__text.get(),
                self.__folder.get(),
            )
            self.event_generate("<<QuestionCreated>>")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
