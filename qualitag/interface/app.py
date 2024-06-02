import customtkinter as ctk
from widgets.tags import TagView

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # App settings
        self.title("QualiTag")
        self.geometry("800x600")
        self.resizable(False, False)

        # Build the app
        self.__build()

    def __build(self):
        # Build the app widgets
        self.lateral_bar = ctk.CTkFrame(self, width=150)
        self.main_frame = ctk.CTkFrame(self, bg_color="white")

        # Pack the app widgets
        self.lateral_bar.pack(side="left", fill="y")
        self.main_frame.pack(side="right", fill="both", expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()
