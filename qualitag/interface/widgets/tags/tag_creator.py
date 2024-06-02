import customtkinter as ctk


class TagCreator(ctk.CTkToplevel):

    def __init__(self, master, tag_manager, **kwargs):
        super().__init__(master=master, **kwargs)

        self.__manager = tag_manager

        # Set window configuration
        self.title("Create a new Tag")
        self.maxsize(854, 480)

        self.__build()

    def __build(self): ...


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
