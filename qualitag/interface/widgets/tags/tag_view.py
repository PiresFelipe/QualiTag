from customtkinter import CTkLabel, CTk
from colour import Color

class Tag:
    name = "Test"
    description = "This is a test tag"
    base_color = "#FF0000"


class TagView(CTkLabel):
    def __init__(self, *args, tag: Tag, width: int = 100, height: int = 32, **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)
        
        self.__tag = tag
        self.__bg = None
        self.__fg = None
        
        self.configure(corner_radius=height, fg_color=self.background, text_color=self.foreground, text=self.__tag.name)

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

        If the foreground color is not set, it calculates the foreground color based on the base color.
        The foreground color is calculated by updating the HSL value of the base color with a luminance of 0.25.
        """
        if self.__fg is None:
            self.__fg = Color(self.__tag.base_color)
            self.__fg.set_luminance(0.25)
            self.__fg = self.__fg.get_hex_l()
        return self.__fg


if __name__ == "__main__":
    root = CTk()
    tg = TagView(
        root,
        tag = Tag(),
    )
    tg.pack()
    root.mainloop()
