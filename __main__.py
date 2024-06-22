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

        self.__tag_manager.create_tag("Teste", "#ff0000")
        self.__tag_manager.create_tag("verde", "#00ff00")
        self.__tag_manager.create_tag("azul", "#0000ff")

        ctk.CTkButton(self, text="Create Tag", command=self.open_tag_creator).pack(
            side="left"
        )

        qtg.TagsList(
            self, manager=self.__tag_manager, events=self.__events_manager
        ).pack(fill="y", expand=True, side="left")
        
        code = qtg.CodingBox(
            self, tags_manager=self.__tag_manager, events=self.__events_manager
        )
        code.pack(fill="both", expand=True, side="right")

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
