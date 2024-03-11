from typing import Tuple
from customtkinter import CTkToplevel, CTkEntry, CTk, CTkButton


class TagCreator(CTkToplevel):

    def __init__(self, *args, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)

        self.title("Create a new tag")
        self.__name_input = CTkEntry(self)
        self.focus()
