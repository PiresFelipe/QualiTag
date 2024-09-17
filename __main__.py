from tkinter import filedialog, messagebox
from typing import Tuple

import customtkinter as ctk

import qualitag as qtg
from qualitag.interface.utils import fonts
from qualitag.src import CodingProject


class App(ctk.CTk):

    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        # App settings
        self.title("QualiTag")
        self.geometry("800x670")

        # App layout
        self.__first_line = ctk.CTkFrame(self)
        self.__main_content = ctk.CTkFrame(self)

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
        self.__dashboard_screen = None

        self.start_screen()

    def start_screen(self):
        self.__init_screen = ctk.CTkFrame(self, fg_color="transparent")

        # Create label
        _font = ctk.CTkFont(**fonts["h1"])
        _font.configure(size=40)
        label = ctk.CTkLabel(
            self.__init_screen,
            text="Bem-vindo ao QualiTag!",
            font=_font,
            pady=20,
        )

        label.pack()

        # Create buttons
        _font = ctk.CTkFont(**fonts["h2"])
        new_project_button = ctk.CTkButton(
            self.__init_screen,
            text="Começar um novo projeto",
            command=self.new_project,
            font=_font,
            width=_font.measure("Começar um novo projeto") + 30,
        )
        new_project_button.pack(pady=10)

        open_project_button = ctk.CTkButton(
            self.__init_screen,
            text="Abrir um projeto existente",
            command=self.load_project,
            font=_font,
            width=_font.measure("Abrir um projeto existente") + 30,
        )
        open_project_button.pack(pady=10)

        self.__init_screen.place(relx=0.5, rely=0.5, anchor="center")

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
            self.__tabview = ctk.CTkTabview(
                self.__main_content, command=self.on_tab_change
            )
            self.__tabview.add("Projeto")
            self.open_project_screen(self.__tabview.tab("Projeto"))
            self.__tabview.add("Tags")
            self.open_tags_screen(self.__tabview.tab("Tags"))
            # self.__tabview.add("Dashboard")
            # self.open_dashboard_screen(self.__tabview.tab("Dashboard"))

            qtg.FileMenu(self.__first_line, project=self.__project).pack(
                fill="x", expand=True
            )

            self.__first_line.pack(fill="x", expand=False)
            self.__main_content.pack(fill="both", expand=True)
            self.__tabview.pack(fill="both", expand=True)
        return self.__tabview

    def on_tab_change(self):
        tab = self.__tabview.get()
        if tab == "Tags":
            self.__tags_screen.tags_counter.update_tags()

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
        self.__tags_screen = qtg.TagsScreen(
            parent,
            project=self.__project,
            create_fn=self.open_tag_creator,
            event_manager=self.__events_manager,
        )
        self.__tags_screen.pack(fill="both", expand=True)

    def open_dashboard_screen(self, parent):
        self.__dashboard_screen = qtg.DashboardScreen(parent, project=self.__project)
        self.__dashboard_screen.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()
