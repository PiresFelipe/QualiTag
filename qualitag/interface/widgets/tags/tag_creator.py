import customtkinter as ctk
from tkinter import StringVar
from qualitag.interface.widgets.tags.tag_views import TagPreview


class TagCreator(ctk.CTkToplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = StringVar()
        self.description = StringVar()
        self.color = StringVar()
        self.color.set("#ffffff")

        self.__tag = {
            "name": self.name,
            "color": self.color,
            "desc": self.description,
        }

        # Set window configuration
        self.title("Create a new Tag")
        self.geometry("400x300")
        self.resizable(False, False)

        self.__grid_config()
        self.__build()

    def __grid_config(self):
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=2)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=3)

        for i in range(5):
            self.grid_columnconfigure(i, weight=1)

    def __build(self):

        # Tag previewer
        self.__viewer = TagPreview(self, tag=self.__tag)
        self.__viewer.grid(row=0, column=0, columnspan=5, pady=10, ipady=5)

        # Name input
        ctk.CTkLabel(self, text="Nome da tag:").grid(
            row=1, column=0, columnspan=4, sticky="w", padx=10
        )
        self.__name_input = ctk.CTkEntry(self, textvariable=self.name)
        self.__name_input.grid(
            row=2, column=0, columnspan=4, sticky="ew", pady=[0, 10], padx=10
        )
        self.after(300, self.__name_input.focus)

        # Color input
        ctk.CTkLabel(self, text="Cor da tag:").grid(
            row=1, column=4, sticky="w", padx=10
        )
        self.__color_input = ctk.CTkEntry(self, textvariable=self.color)
        self.__color_input.grid(row=2, column=4, sticky="ew", pady=[0, 10], padx=10)

        # Description input
        ctk.CTkLabel(self, text="Descrição da tag:\t(opcional)").grid(
            row=3, column=0, columnspan=5, sticky="w", padx=10
        )

        self.__description_input = ctk.CTkTextbox(self, border_width=2)
        self.__description_input.grid(
            row=4, column=0, columnspan=5, sticky="nsew", padx=10, pady=[0, 10]
        )
