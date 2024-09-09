import customtkinter as ctk
from ..shared.questions_selector import QuestionsSelector


class ProjectScreen(ctk.CTkFrame):

    def __init__(self, *args, project, new_question_fn, **kwargs):
        super().__init__(*args, **kwargs)

        self.__project = project

        # Create label
        label = ctk.CTkLabel(
            self,
            text="Project Screen",
            font=("Arial", 24),
            pady=20,
        )
        label.pack()

        # Button to add question
        add_question_button = ctk.CTkButton(
            self, text="Nova questão", command=new_question_fn
        )
        add_question_button.pack(pady=10)

        # Questions list
        questions_list = QuestionsSelector(self, questions=project.questions)
        questions_list.pack()
