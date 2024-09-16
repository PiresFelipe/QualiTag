import customtkinter as ctk


class ImageDisplay(ctk.CTkFrame):

    def __init__(self, *args, title: str, image, **kwargs):
        super().__init__(*args, **kwargs)

        self.__title = ctk.CTkLabel(self, text=title)

        self.__title.pack(side="top", fill="x")
