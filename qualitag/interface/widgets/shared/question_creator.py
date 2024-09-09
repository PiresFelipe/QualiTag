import customtkinter as ctk
from tkinter import filedialog, StringVar
import os


class QuestionCreator(ctk.CTkToplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Create a new Question")

        self.__folder = StringVar()
        self.__folder.trace_add(mode="write", callback=self.check_folder)

        ctk.CTkLabel(self, text="Qual foi a pergunta realizada?").pack(fill="x")
        ctk.CTkEntry(self).pack(fill="x", padx=10)

        ctk.CTkLabel(self, text="Selecione a pasta com as respostas").pack(fill="x")
        ctk.CTkLabel(
            self,
            text="* lembre-se que as repostas devem estar em formato PDF e em arquivos separados",
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

        self.__error_label = ctk.CTkLabel(self, text="", text_color="red")
        self.__error_label.pack(fill="x", pady=10)

        self.__btn = ctk.CTkButton(self, text="Criar", state="disabled")
        self.__btn.pack(pady=10)

    def check_folder(self, *args):
        if not self.valid_folder():
            self.__error_label.configure(
                text="A pasta selecionada não contém arquivos PDF"
            )
            self.__btn.configure(state="disabled")
        else:
            self.__error_label.configure(text="")
            self.__btn.configure(state="normal")

    def valid_folder(self) -> bool:

        for file in os.listdir(self.__folder.get()):
            if file.endswith(".pdf"):
                return True
        return False
