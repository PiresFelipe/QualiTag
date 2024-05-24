from customtkinter import CTkButton
from colour import Color
from widgets.tags.tags_manager import TagsManager


class TagView(CTkButton):
    def __init__(
        self,
        *args,
        tag,
        manager: TagsManager | None = None,
        width: int = 100,
        height: int = 32,
        **kwargs,
    ):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.__tag = tag
        self.__event = manager.events
        self.__bg = None
        self.__fg = None

        self.configure(
            corner_radius=height,
            border_width=max(1, int(width * 0.02)),
            fg_color=self.background,
            border_color=self.foreground,
            text_color=self.foreground,
            text=self.__tag.name,
            hover_color=self.hover_color,
            cursor="hand2",
        )

        if manager is not None:
            self._command = self.__on_click

    def __on_click(self, _):
        self.__event.generate_event(self)

    @property
    def name(self):
        """Name of associated tag."""
        return self.__tag.name

    @property
    def background(self):
        """
        Returns the background color of the tag view.

        If the background color has not been set, it calculates a new color based on the base color
        by adjusting the luminance to 0.9.
        """
        if self.__bg is None:
            self.__bg = Color(self.__tag.base_color)
            self.__bg.set_luminance(0.9)
            self.__bg = self.__bg.get_hex_l()
        return self.__bg

    @property
    def foreground(self):
        """
        Returns the foreground color of the tag view.

        If the foreground color is not set, it calculates the foreground
        color based on the base color.
        The foreground color is calculated by updating the HSL value
        of the base color with a luminance of 0.25.
        """
        if self.__fg is None:
            self.__fg = Color(self.__tag.base_color)
            self.__fg.set_luminance(0.25)
            self.__fg = self.__fg.get_hex_l()
        return self.__fg

    @property
    def hover_color(self):
        """
        Returns the hover color of the tag view.

        The hover color is calculated by updating the HSL value of the base color
        with a luminance of 0.8.
        """
        hover = Color(self.__tag.base_color)
        hover.set_luminance(0.8)
        return hover.get_hex_l()
