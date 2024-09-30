from tkinter import messagebox
from typing import Optional

import customtkinter as ctk

from qualitag.interface.utils.event_observer import Event

from ....src import Tag, CodingProject
from ...utils import fonts
from ...utils.event_observer import Observer


class TagDescriptor(ctk.CTkFrame, Observer):

    def __init__(self, *args, project: CodingProject, events_manager, **kwargs):
        super().__init__(*args, **kwargs)

        self.__project = project
        self.__manager = project.tags_manager
        self.__events_manager = events_manager
        self.__tags: list = []
        self.__selected_tag: Optional[Tag] = None

        self.__list = ctk.CTkScrollableFrame(self)
        self.__list.pack(fill="both", expand=True, side="left", padx=10)

        # Layout
        self.__del_col = ctk.CTkFrame(self.__list)
        self.__del_col.grid(column=0, row=0, sticky="nsew")
        self.__name_col = ctk.CTkFrame(self.__list)
        self.__name_col.grid(column=1, row=0, sticky="nsew")
        self.__count_col = ctk.CTkFrame(self.__list)
        self.__count_col.grid(column=2, row=0, sticky="nsew")

        self.__list.grid_columnconfigure(0, weight=1)
        self.__list.grid_columnconfigure(1, weight=4)
        self.__list.grid_columnconfigure(2, weight=1)

        self.__description = ctk.CTkFrame(self)
        self.__description.pack(fill="both", expand=True, side="right", padx=10)

        self.__desc_title = ctk.CTkLabel(
            self.__description,
            text="Selecione uma tag",
            justify="left",
            anchor="w",
            font=ctk.CTkFont(weight="bold", size=24),
        )
        self.__desc_title.pack(fill="x", padx=10)

        self.__desc_text = ctk.CTkTextbox(
            self.__description, fg_color=self.cget("bg_color")[0], state="disabled"
        )
        self.__desc_text.pack(fill="both", expand=True, padx=10)

        self.update_tags()

    @property
    def selected_tag(self):
        return self.__selected_tag

    def update_tags(self):
        for _ in range(len(self.__tags)):
            _tag = self.__tags.pop()
            for widget in _tag:
                widget.destroy()

        for tag in self.__manager.get_all_tags(sort=True):
            self.add_tag(tag)

    def add_tag(self, tag: Tag):
        font = ctk.CTkFont(**fonts["h3"])
        _del_btn = ctk.CTkButton(
            self.__del_col,
            text="X",
            command=lambda: self.delete_tag(tag.name),
            font=font,
            width=font.measure("X") + 10,
        )
        _del_btn.pack(pady=[0, 10])

        _text = ctk.CTkLabel(
            self.__name_col,
            text=tag.name,
            text_color=tag.color,
            font=font,
        )
        _text.pack(pady=[0, 10], fill="x", expand=True)
        _text.bind("<Button-1>", lambda _: self.change_description(tag))

        _count = ctk.CTkLabel(
            self.__count_col, text=str(self.__manager.counter.get_count(tag.name)), font=font
        )
        _count.pack(pady=[0, 10], fill="x", expand=True)
        _count.bind("<Button-1>", lambda _: self.change_description(tag))

        self.__tags.append((_del_btn, _text, _count))

    def delete_tag(self, tag_name: str):
        if messagebox.askyesno(
            "Deletar tag", f"Você tem certeza que deseja deletar a tag '{tag_name}'?"
        ):
            self.after(
                100, lambda: self.__events_manager.generate_event("deleted", tag_name)
            )
            self.__project.delete_tag(tag_name)
            self.update_tags()

    def on_event(self, event: Event):
        if event.event_type == "created":
            self.update_tags()

    def change_description(self, tag: Tag):
        title = tag.name if len(tag.name) < 15 else tag.name[:12] + "..."

        if tag.description is None or tag.description == "":
            description = "Nenhuma descrição disponível."
        else:
            description = tag.description

        self.__desc_title.configure(text=title, text_color=tag.color)

        self.__desc_text.configure(state="normal")
        self.__desc_text.delete("1.0", "end")
        self.__desc_text.insert("1.0", description)
        self.__desc_text.configure(state="disabled")
