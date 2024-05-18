import customtkinter as ctk


class LateralBar(ctk.CTkFrame):

    def __init__(self, master, title: str, **kwargs):
        super().__init__(master, **kwargs)

        if "font" in kwargs:
            self.__font = kwargs["font"]
        else:
            self.__font = ("Arial", 12)

        self.__build(title)

    def __build(self, title: str):
        self.__frame = ctk.CTkScrollableFrame(
            self,
            label_text=title,
            label_font=self.__font,
            label_anchor="w",
            label_fg_color="transparent",
        )
        self.__frame.pack(side="top", fill="both", expand=True)
