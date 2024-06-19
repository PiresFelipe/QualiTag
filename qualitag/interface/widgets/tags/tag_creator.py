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
        self.maxsize(854, 480)

        self.__build()

    def __build(self):

        self.__viewer = TagPreview(self, tag=self.__tag)
        self.__viewer.pack()
        
        self.__name_input = ctk.CTkEntry(self, textvariable=self.name)
        self.__name_input.pack()
        self.after(10, self.__name_input.focus)
        
        self.__color_input = ctk.CTkEntry(self, textvariable=self.color)
        self.__color_input.pack()
        
        self.__description_input = ctk.CTkTextbox(self)
        self.__description_input.pack()
