from customtkinter import CTkFrame, CTkLabel, CTk


class TagView(CTkFrame):
    def __init__(
        self,
        *args,
        width: int = 100,
        height: int = 32,
        **kwargs
    ):
        super().__init__(*args, width=width, height=height, **kwargs)
        self.configure(corner_radius = 32, border_width = 2, border_color = "black")
        

if __name__ == "__main__":
    root = CTk()
    tag = TagView(root)
    tag.pack()
    root.mainloop()
