from typing import Tuple
import customtkinter as ctk
import qualitag as qtg
from tkinter import filedialog, messagebox
from qualitag.src import CodingProject


class App(ctk.CTk):

    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        # App settings
        self.title("QualiTag")
        self.geometry("800x600")

        # App attributes
        self.__project: CodingProject = CodingProject()
        self.__tag_manager = self.__project.tags_manager
        self.__events_manager = qtg.TagEventsManager()

        # App screens
        self.__tabview: ctk.CTkTabview = None
        self.__tag_creator = None
        self.__question_creator = None
        self.__init_screen = None
        self.__code_screen = None
        self.__tags_screen = None
        self.__projects_screen = None
        self.__dashboard = None

        self.start_screen()

    def start_screen(self):
        self.__init_screen = ctk.CTkFrame(self)

        # Create label
        label = ctk.CTkLabel(
            self.__init_screen,
            text="Bem-vindo ao QualiTag!",
            font=("Arial", 24),
            pady=20,
        )
        label.pack()

        # Create buttons
        new_project_button = ctk.CTkButton(
            self.__init_screen, text="Começar um novo projeto", command=self.new_project
        )
        new_project_button.pack(pady=10)

        open_project_button = ctk.CTkButton(
            self.__init_screen,
            text="Abrir um projeto existente",
            command=self.load_project,
        )
        open_project_button.pack(pady=10)

        self.__init_screen.pack(fill="both", expand=True)

    def load_project(self):

        _file = filedialog.askopenfilename(filetypes=[("QualiTag project", "*.pkl")])

        try:
            self.__project = qtg.CodingProject.load(_file)
            self.__tag_manager = self.__project.tags_manager
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

        self.__init_screen.destroy()
        self.get_tabview()

    def new_project(self):
        self.__init_screen.destroy()
        self.get_tabview()

    def get_tabview(self) -> ctk.CTkTabview:
        if self.__tabview is None or not self.__tabview.winfo_exists():
            self.__tabview = ctk.CTkTabview(self)
            self.__tabview.add("Projeto")
            self.open_project_screen(self.__tabview.tab("Projeto"))
            self.__tabview.add("Tags")
            self.open_tags_screen(self.__tabview.tab("Tags"))
            self.__tabview.add("Dashboard")
            self.__tabview.pack(fill="both", expand=True)
        return self.__tabview

    def save_project(self):

        _file = filedialog.asksaveasfilename(
            filetypes=[("QualiTag project", "*.pkl")], confirmoverwrite=True
        )

        try:
            self.__project.save(_file)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

    def open_tag_creator(self):
        if self.__tag_creator is None or not self.__tag_creator.winfo_exists():
            self.__tag_creator = qtg.TagCreator(
                self, manager=self.__tag_manager, events=self.__events_manager
            )
            self.__tag_creator.grab_set()
        else:
            self.__tag_creator.focus()

    def open_add_question(self):
        if (
            self.__question_creator is None
            or not self.__question_creator.winfo_exists()
        ):
            self.__question_creator = qtg.QuestionCreator(self, project=self.__project)
            self.__question_creator.bind(
                "<<QuestionCreated>>", self.__projects_screen.on_question_created
            )
            self.__question_creator.grab_set()
        else:
            self.__question_creator.focus()

    def open_coding_screen(self, parent):
        self.__code_screen = qtg.CodingScreen(
            parent,
            question=None,
            tags_mng=self.__tag_manager,
            events=self.__events_manager,
        )
        self.__code_screen.pack(fill="both", expand=True)

    def open_project_screen(self, parent):
        self.__projects_screen = qtg.ProjectScreen(
            parent,
            project=self.__project,
            new_question_fn=self.open_add_question,
            events=self.__events_manager,
        )
        self.__projects_screen.pack(fill="both", expand=True)

    def open_tags_screen(self, parent):
        tags_screen = qtg.TagsScreen(
            parent,
            tags_manager=self.__tag_manager,
            create_fn=self.open_tag_creator,
            event_manager=self.__events_manager,
        )
        tags_screen.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()
