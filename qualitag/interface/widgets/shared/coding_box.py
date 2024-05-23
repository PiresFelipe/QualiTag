import customtkinter as ctk
from tkinter import TclError
from utils import Observer
from widgets.tags import TagsManager


class CodingBox(ctk.CTkTextbox, Observer):

    def __init__(self, master, tags_manager: TagsManager, **kwargs):
        assert isinstance(
            tags_manager, TagsManager
        ), "tags_manager must be an instance of TagsManager"

        super().__init__(master, **kwargs)

        # Subcribing to tags_manager events
        tags_manager.events.attach(self)

        # Binding selection events
        self.bind("<B1-Motion> <ButtonRelease-1>", self.__on_select)
        self.bind("<Double-Button-1>", self.__on_select)

    def __on_select(self, event):

        self.after(3, self.get_selection)

    def get_selection(self, as_index=False) -> tuple[str, str] | str | None:
        """
        Get the selected text or indices in the coding box.

        Parameters:
        ---
            as_index (bool, optional): If True, returns the indices of the selected text.
                If False, returns the selected text. Defaults to False.

        Returns:
        ---
            tuple[str, str] | str | None: If as_index is True, returns a tuple of the indices
                of the selected text. If as_index is False, returns the selected text.
                If no text is selected, returns None.
        """
        try:
            if as_index:
                return self.index("sel.first"), self.index("sel.last")
            return self.get("sel.first", "sel.last")
        except TclError:
            return None

    def on_event(self, event):

        if self.winfo_exists():
            selection = self.get_selection(as_index=True)
            if selection is not None:
                self.tag_add(event.state['name'], *selection)
                self.tag_config(event.state['name'], background=event.state['color'])
