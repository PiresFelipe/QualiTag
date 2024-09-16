import customtkinter as ctk
from tkinter import StringVar
from ..shared import QuestionsSelector, AnswerSelector
from ..tags import TagsList
from ...utils import fonts
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

        # Screen layout
        self.__title_line = ctk.CTkFrame(self)
        self.__coding_content = ctk.CTkFrame(self)
        self.__tags_col = ctk.CTkFrame(self)

        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)

        self.__title_line.grid(row=0, column=0, sticky="ew", columnspan=2)
        self.__coding_content.grid(row=1, column=0, sticky="nsew")
        self.__tags_col.grid(row=1, column=1, sticky="nsew")

        # Create label
        label = ctk.CTkLabel(
            self.__title_line,
            text="Projeto de codificação".upper(),
            font=ctk.CTkFont(**fonts["h1"]),
        )
        label.grid(row=0, column=0, sticky="w", columnspan=2)

        # Button to add question
        add_question_button = ctk.CTkButton(
            self.__title_line, text="Nova questão", command=new_question_fn
        )
        add_question_button.grid(row=1, column=1, pady=10, padx=10)

        # Questions list
        _font = ctk.CTkFont(**fonts["h3"])
        self.__questions_list = QuestionsSelector(
            self.__title_line,
            questions=project.questions,
            font=_font,
            width=_font.measure("Questão 000") + 100,
        )
        self.__questions_list.selected.trace_add("write", self.change_question)
        self.__questions_list.grid(row=1, column=0)

        # Tags list
        TagsList(
            self.__tags_col,
            manager=self.__project.tags_manager,
            events=self.__events,
            height=440,
        ).pack(fill="both", expand=True, pady=10, padx=10)

        # Question label
        self.__text = StringVar()
        ctk.CTkLabel(
            self.__coding_content,
            textvariable=self.__text,
            font=ctk.CTkFont(**fonts["body"]),
            text="",
            wraplength=400,
        ).pack(fill="x", anchor="w")

        # No question selected message
        self.__warning_label = ctk.CTkLabel(
            self.__coding_content,
            text="Crie ou selecione uma questão para começar",
            text_color="red",
            font=ctk.CTkFont(**fonts["h3"]),
        )
        self.__warning_label.pack(fill="both", expand=True)

        self.on_question_created(None)

    def on_question_created(self, _):
        for new_question in self.__project.questions[len(self.__questions_frames) :]:
            self.__questions_frames.append(
                (
                    new_question,
                    AnswerSelector(
                        self.__coding_content,
                        question=new_question,
                        events=self.__events,
                        tags_mng=self.__project.tags_manager,
                    ),
                )
            )
        self.__questions_list.update_questions()

    def change_question(self, *_):
        self.__warning_label.destroy()
        if self.__current_question is not None:
            self.__current_question.pack_forget()

        idx = self.__questions_list.selected.get()
        question = self.__questions_frames[idx][1]
        self.__text.set(self.__questions_frames[idx][0].question)
        question.pack(fill="both", expand=True)
        self.__current_question = question
