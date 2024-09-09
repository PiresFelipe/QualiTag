from typing import TypedDict
from tkinter import StringVar

from customtkinter import CTkButton
from colour import Color
from qualitag.interface.utils.tags_events import TagEventsManager
from qualitag.src import Tag


class TagPrototype(TypedDict):
    name: StringVar
    color: StringVar


class TagView(CTkButton):

    def __init__(
        self,
        *args,
        tag: Tag,
        events_manager: TagEventsManager,
        width: int = 100,
        height: int = 32,
        **kwargs
    ):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.__tag = tag
        self.__event = events_manager

        self.configure(
            corner_radius=height,
            border_width=max(1, int(width * 0.02)),
            fg_color=self.background,
            border_color=self.foreground,
            text_color=self.foreground,
            text=self.name,
            hover_color=self.hover_color,
            cursor="hand2",
            command=self.__on_click,
        )

    def __on_click(self):
        self.__event.generate_event("clicked", self)

    @property
    def name(self):
        if len(self.__tag.name) > 10:
            return self.__tag.name[:10] + "..."
        return self.__tag.name
    @property
    def full_name(self):
        return self.__tag.name

    @property
    def background(self):
        color = Color(self.__tag.color)
        color.set_luminance(0.9)
        return color.get_hex_l()

    @property
    def foreground(self):
        color = Color(self.__tag.color)
        color.set_luminance(0.25)
        return color.get_hex_l()

    @property
    def hover_color(self):
        color = Color(self.__tag.color)
        color.set_luminance(0.8)
        return color.get_hex_l()


class TagPreview(CTkButton):

    def __init__(
        self, *args, tag: TagPrototype, width: int = 100, height: int = 32, **kwargs
    ):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.__name = tag["name"]
        self.__color = tag["color"]

        self.configure(
            corner_radius=height,
            border_width=max(1, int(width * 0.02)),
            fg_color=self.background,
            border_color=self.foreground,
            text_color=self.foreground,
            text=self.name,
            hover_color=self.hover_color,
            cursor="hand2",
        )

        self.__name.trace_add("write", self.__update_view)
        self.__color.trace_add("write", self.__update_view)

    def __update_view(self, _var, *_):
        if _var == str(self.__name):
            self.configure(text=self.name)
        elif _var == str(self.__color):
            if len(self.__color.get()) == 7 or len(self.__color.get()) == 4:
                self.configure(
                    fg_color=self.background,
                    border_color=self.foreground,
                    text_color=self.foreground,
                    hover_color=self.hover_color,
                )

    @property
    def name(self):
        if len(self.__name.get()) > 10:
            return self.__name.get()[:10] + "..."
        return self.__name.get()

    @property
    def background(self):
        color = Color(self.__color.get())
        color.set_luminance(0.9)
        return color.get_hex_l()

    @property
    def foreground(self):
        color = Color(self.__color.get())
        color.set_luminance(0.25)
        return color.get_hex_l()

    @property
    def hover_color(self):
        color = Color(self.__color.get())
        color.set_luminance(0.8)
        return color.get_hex_l()
