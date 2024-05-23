from tkinter import StringVar
from ttkbootstrap.colorutils import update_hsl_value
from ttkbootstrap.tooltip import ToolTip
from customtkinter import CTkFrame, CTkLabel


class TagView(CTkFrame):

    def __init__(
        self,
        *args,
        width: int = 500,
        height: int = 500,
        tag: dict[str, str | StringVar],
        **kwargs
    ):
        super().__init__(*args, width=width, height=height, **kwargs)

        # self.__init_vars(tag)
        # self.__build()

    def __init_vars(self, tag: dict[str, str | StringVar]):
        if isinstance(tag["name"], StringVar):
            self.name = tag["name"]
        else:
            self.name = StringVar(self, tag["name"])

        if isinstance(tag["description"], StringVar):
            self.description = tag["description"]
        else:
            self.description = StringVar(self, tag["description"])

        if isinstance(tag["color"], StringVar):
            self.base_color = tag["color"]
        else:
            self.base_color = StringVar(self, tag["color"])

        self.__bg = None
        self.__fg = None

    def __build(self):
        CTkLabel(self, textvariable=self.name, text_color=self.foreground).pack(
            side="left", fill="both"
        )

        tooltip_text = self.description.get()
        if tooltip_text and len(tooltip_text) > 0:
            tooltip_text = (
                tooltip_text if len(tooltip_text) < 150 else tooltip_text[:100] + "..."
            )
            ToolTip(self, tooltip_text, delay=0.5)

    @property
    def background(self):
        """
        Returns the background color of the tag view.

        If the background color has not been set, it calculates a new color based on the base color
        by adjusting the luminance to 0.75.
        """
        if self.__bg is None:
            self.__bg = update_hsl_value(
                self.base_color, lum=0.75, inmodel="hex", outmodel="hex"
            )
        return self.__bg

    @property
    def foreground(self):
        """
        Returns the foreground color of the tag view.

        If the foreground color is not set, it calculates the foreground color based on the base color.
        The foreground color is calculated by updating the HSL value of the base color with a luminance of 0.25.
        """
        if self.__fg is None:
            self.__fg = update_hsl_value(
                self.base_color, lum=0.25, inmodel="hex", outmodel="hex"
            )
        return self.__fg


if __name__ == "__main__":
    from customtkinter import CTk

    root = CTk()

    tag = {
        "name": "Tag Name",
        "description": "This is a tag description",
        "color": "#ff0000",
    }

    tag_view = TagView(root, tag=tag)
    tag_view.pack()

    root.mainloop()
