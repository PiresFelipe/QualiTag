import customtkinter as ctk
from tkinter import StringVar
from qualitag.interface.widgets.tags.tag_view import TagView

class TagCreator(ctk.CTkToplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = StringVar()
        self.description = StringVar()
        self.color = StringVar()

        # Set window configuration
        self.title("Create a new Tag")
        self.maxsize(854, 480)

        self.__build()

    def __build(self):

        #self.__viewer = TagView(self, self.__manager)
        self.__name_input = ctk.CTkEntry(self, textvariable=self.name)
        self.__description_input = ctk.CTkTextbox(self)

        self.__name_input.pack()
        self.__description_input.pack()


if __name__ == "__main__":

    def open_toplevel(creator):
        if creator is None or not creator.winfo_exists():
            creator = TagCreator(root, None)
        else:
            creator.focus()
        return creator

    root = ctk.CTk()
    creator = None

    btn = ctk.CTkButton(
        root, text="open toplevel", command=lambda: open_toplevel(creator)
    )
    btn.pack(side="top", padx=20, pady=20)

    root.mainloop()
