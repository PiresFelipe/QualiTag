from typing import Tuple
import customtkinter as ctk
import qualitag as qtg


class App(ctk.CTk):

    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        # App settings
        self.title("QualiTag")
        self.geometry("800x600")

        # App attributes
        self.__tag_manager = qtg.TagsManager()
        self.__events_manager = qtg.TagEventsManager()
        self.__tag_creator = None

        ctk.CTkButton(self, text="Create Tag", command=self.open_tag_creator).pack()

        qtg.TagsList(
            self, manager=self.__tag_manager, events=self.__events_manager
        ).pack(fill="y", expand=True)

    def open_tag_creator(self):
        if self.__tag_creator is None or not self.__tag_creator.winfo_exists():
            self.__tag_creator = qtg.TagCreator(
                self, manager=self.__tag_manager, events=self.__events_manager
            )
            self.__tag_creator.grab_set()
        else:
            self.__tag_creator.focus()


if __name__ == "__main__":
    app = App()
    app.mainloop()
