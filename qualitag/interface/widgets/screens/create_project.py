import os
import customtkinter as ctk
from tkinter import filedialog

from qualitag import Answer, import_data


class CreateProjectScreen(ctk.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        title = ctk.CTkFont("Arial black", 20, "bold")
        subtitle = ctk.CTkFont("Arial", 20)
        
        ctk.CTkLabel(self, text="Bem-vindo ao QualiTag!", font=title).pack(pady=20)
        
        ctk.CTkLabel(self, text="Para começar, inicialmente escreva a pergunta que gerou as respostas\ne importe os arquivos PDF que deseja analisar", font=subtitle).pack(pady=[0,10])
        
        question = ctk.CTkEntry(self, font=subtitle, placeholder_text="Digite a pergunta aqui")
        question.pack(fill="x", padx=100)

        ctk.CTkButton(self, text="Import data", command=self.__import_data).place(relx=0.5, rely=0.5, anchor="center")
        
    
    def __import_data(self) -> list[Answer]:
        data = []
        folder = filedialog.askdirectory()
        print(folder)
        for file in os.listdir(folder):
            if file.endswith(".pdf"):
                data.append(import_data(os.path.join(folder, file)))
        
        return data
