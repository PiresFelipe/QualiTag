import customtkinter as ctk
from tkinter import StringVar, messagebox
from qualitag.interface.widgets.tags.tag_views import TagPreview
from qualitag.src.tags.tags_manager import TagsManager
from qualitag.interface.utils.tags_events import TagEventsManager


class TagCreator(ctk.CTkToplevel):

    def __init__(self, *args, manager: TagsManager, events: TagEventsManager, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = StringVar()
        self.color = StringVar()
        self.color.set("#ffffff")

        self.__tag_manager = manager
        self.__events = events

        # Set window configuration
        self.title("Create a new Tag")
        self.geometry("500x350")
        self.resizable(False, False)

        self.__grid_config()
        self.__build()

    def __grid_config(self):
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=2)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=2)
        self.grid_rowconfigure(5, weight=2)

        for i in range(5):
            self.grid_columnconfigure(i, weight=1)

    def __build(self):

        # Tag previewer
        self.__viewer = TagPreview(
            self,
            tag={
                "name": self.name,
                "color": self.color,
            },
        )
        self.__viewer.grid(row=0, column=0, columnspan=5, pady=10, ipady=5)

        # Name input
        ctk.CTkLabel(self, text="Nome da tag:").grid(
            row=1, column=0, columnspan=4, sticky="w", padx=10
        )
        self.__name_input = ctk.CTkEntry(self, textvariable=self.name)
        self.__name_input.grid(
            row=2, column=0, columnspan=4, sticky="ew", pady=[0, 10], padx=10, ipady=5
        )

        # Color input
        ctk.CTkLabel(self, text="Cor da tag:").grid(
            row=1, column=4, sticky="w", padx=10
        )
        self.__color_input = ctk.CTkEntry(self, textvariable=self.color)
        self.__color_input.grid(
            row=2, column=4, sticky="ew", pady=[0, 10], padx=10, ipady=5
        )

        # Description input
        ctk.CTkLabel(self, text="Descrição da tag:\t(opcional)").grid(
            row=3, column=0, columnspan=5, sticky="w", padx=10
        )
        self.__description_input = ctk.CTkTextbox(self, border_width=2)
        self.__description_input.grid(
            row=4, column=0, columnspan=5, sticky="nsew", padx=10, pady=[0, 10]
        )

        # Buttons
        ctk.CTkButton(
            self,
            text="Cancelar",
            command=self.destroy,
            fg_color="transparent",
            hover_color="#dddddd",
            text_color="#666666",
            font=ctk.CTkFont(underline=True),
        ).grid(row=5, column=3, sticky="nse", padx=10, pady=5, ipady=10, ipadx=0)
        ctk.CTkButton(self, text="Criar", command=self.__create_tag).grid(
            row=5, column=4, sticky="nsew", padx=[0, 10], pady=5, ipady=10
        )

    def __create_tag(self):
        try:
            if len(self.color.get()) != 7:
                raise ValueError("Cor inválida, formato aceito: #RRGGBB")

            desc = self.__description_input.get("1.0", "end")
            if len(desc) <= 1:
                desc = None
            tag = self.__tag_manager.create_tag(self.name.get(), self.color.get(), desc)
            self.__events.generate_event("created", tag)
            self.destroy()
        except ValueError as exc:
            messagebox.showerror("Erro ao criar tag", str(exc))
