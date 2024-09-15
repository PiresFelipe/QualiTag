import customtkinter as ctk
from PIL import Image


class ImageDisplay(ctk.CTkFrame):

    def __init__(self, *args, image: Image.Image, title: str, **kwargs):
        super().__init__(*args, **kwargs)

        self.__image = ctk.CTkImage(image)
        self.__title = ctk.CTkLabel(self, text=title)

        self.__title.pack(side="top", fill="x")
        ctk.CTkLabel(self, image=self.__image, text="").pack(
            side="top", fill="both", expand=True
        )

    @property
    def image(self) -> Image.Image:
        return self.__image

    @image.setter
    def image(self, image: Image.Image) -> None:
        self.__image.configure(light_image=image, text="")
        self.master.update_idletasks()

    def set_message(self, message: str) -> None:
        self.__image.configure(text=message, image=None)
        self.master.update_idletasks()
