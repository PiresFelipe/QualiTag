from typing import Optional
import customtkinter as ctk

from qualitag.interface.utils.event_observer import Event
from ...utils.event_observer import Observer
from ....src import Tag
from ....src import TagsManager


class TagDescriptor(ctk.CTkFrame, Observer):

    def __init__(self, *args, tags_manager: TagsManager, **kwargs):
        super().__init__(*args, **kwargs)

        self.__manager = tags_manager
        self.__tags: list = []
        self.__selected_tag: Optional[Tag] = None

        self.__list = ctk.CTkScrollableFrame(self)
        self.__list.pack(fill="both", expand=True, side="left")

        self.__description = ctk.CTkFrame(self)
        self.__description.pack(fill="both", expand=True, side="right")

        self.__desc_title = ctk.CTkLabel(
            self.__description,
            text="Select a tag",
            justify="left",
            anchor="w",
            font=ctk.CTkFont(weight="bold", size=24),
        )
        self.__desc_title.pack(fill="x")

        self.__desc_text = ctk.CTkTextbox(
            self.__description, fg_color=self.cget("bg_color")[0]
        )
        self.__desc_text.pack(fill="both", expand=True)

        self.update_tags()

    @property
    def selected_tag(self):
        return self.__selected_tag

    def update_tags(self):
        for tag in self.__tags:
            tag.destroy()
        
        for tag in self.__manager.get_all_tags(sort=True):
            self.add_tag(tag)

    def add_tag(self, tag: Tag):
        view = ctk.CTkFrame(self.__list)

        _btn = ctk.CTkButton(view, text="X", command=lambda: self.delete_tag(tag.name))
        _btn.grid(column=0, row=0)

        _text = ctk.CTkLabel(
            view, text=tag.name, text_color=tag.color, font=ctk.CTkFont(weight="bold")
        )
        _text.grid(column=1, row=0)
        _text.bind("<Button-1>", lambda _: self.change_description(tag))

        _count = ctk.CTkLabel(view, text=str(self.__manager.get_count(tag.name)))
        _count.grid(column=2, row=0)
        _count.bind("<Button-1>", lambda _: self.change_description(tag))

        # On click on this line
        view.bind("<Button-1>", lambda _: self.change_description(tag))
        # view.bind("<Enter>", lambda _: view.configure(bg_color="#E0E0E0"))
        # view.bind("<Leave>", lambda _: view.configure(bg_color="transparent"))
        view.pack()
        self.__tags.append(view)

    def delete_tag(self, tag_name: str):
        print("delete ", tag_name)

    def on_event(self, event: Event):
        if event.event_type == "created":
            print(event.tag)
            self.update_tags()
            

    def change_description(self, tag: Tag):
        title = tag.name if len(tag.name) < 15 else tag.name[:12] + "..."

        if tag.description is None or tag.description == "":
            description = "Nenhuma descrição disponível."
        else:
            description = tag.description

        self.__desc_title.configure(text=title, text_color=tag.color)

        self.__desc_text.delete("1.0", "end")
        self.__desc_text.insert("1.0", description)
