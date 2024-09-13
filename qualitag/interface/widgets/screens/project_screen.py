import customtkinter as ctk
from ..shared import QuestionsSelector, AnswerSelector
from ..tags import TagsList
from qualitag.src import CodingProject, Question


class ProjectScreen(ctk.CTkFrame):

    def __init__(
        self, *args, project: CodingProject, new_question_fn, events, **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.__project = project
        self.__events = events
        self.__current_question = None
        self.__questions_frames: list[tuple[Question, AnswerSelector]] = []

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
        self.__questions_list = QuestionsSelector(self, questions=project.questions)
        self.__questions_list.selected.trace_add("write", self.change_question)
        self.__questions_list.pack()
        
        # Tags list
        TagsList(
            self,
            manager=self.__project.tags_manager,
            events=self.__events,
            height=440,
        ).pack(fill="both", expand=True, pady=10, padx=10)

    def on_question_created(self, _):
        for new_question in self.__project.questions[len(self.__questions_frames) :]:
            self.__questions_frames.append(
                (
                    new_question,
                    AnswerSelector(
                        self,
                        question=new_question,
                        events=self.__events,
                        tags_mng=self.__project.tags_manager,
                    ),
                )
            )
        self.__questions_list.update_questions()

    def change_question(self, *_):
        if self.__current_question is not None:
            self.__current_question.pack_forget()
            
        idx = self.__questions_list.selected.get()
        question = self.__questions_frames[idx][1]
        question.pack(fill="both", expand=True)
        self.__current_question = question
