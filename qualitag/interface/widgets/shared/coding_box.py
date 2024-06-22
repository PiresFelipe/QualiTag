from typing import Optional
import customtkinter as ctk
from tkinter import TclError, Event
from qualitag.interface.utils import Observer
from qualitag.interface.utils import TagEventsManager
from qualitag.src import TagsManager


class CodingBox(ctk.CTkTextbox, Observer):

    def __init__(
        self, master, tags_manager: TagsManager, events: TagEventsManager, **kwargs
    ):
        assert isinstance(
            tags_manager, TagsManager
        ), "tags_manager must be an instance of TagsManager"

        super().__init__(master, **kwargs)

        self.__debounce: Optional[str] = None

        # Subcribing to tags_manager events
        events.attach(self)
        
        self.set_text("lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua")

    def set_text(self, text: str):
        """
        Set the text of the coding box.

        Parameters:
        ---
            text (str): Text to be set in the coding box.
        """
        self.configure(state="normal")
        self.delete("1.0", "end")
        self.insert("1.0", text)
        self.configure(state="disabled")

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

    def get_codes(self):
        """
        Get the tags in this text and texts associated.

        Returns:
        ---
            dict[str, list[str]]: List of codes in the coding box.
        """
        tags = self.tag_names()
        codes = {}
        for tag in tags:
            if tag == "sel":
                continue
            codes[tag] = self.tag_ranges(tag)
        print(codes)   
        return codes

    def on_event(self, event):
        if self.winfo_exists() and event.event_type == "clicked":
            selection = self.get_selection(as_index=True)
            if selection is not None:
                self.tag_add(event.tag.full_name, *selection)
                self.tag_config(
                    event.tag.full_name,
                    background=event.tag.background,
                    foreground=event.tag.foreground,
                )
                self.tag_bind(
                    event.tag.full_name,
                    "<Button-3>",
                    lambda e: self.remove_tag(e, event.tag.full_name),
                )
                self.tag_remove("sel", "sel.first", "sel.last")
                self.tag_raise("sel")

    def remove_tag(self, event: Event, tag_name: str):
        # get the index of the mouse click
        index = event.widget.index(f"@{event.x},{event.y}")

        # get the indices of all "adj" tags
        tag_indices = self.tag_prevrange(tag_name, index)
        if len(tag_indices) == 0:
            tag_indices = self.tag_nextrange(tag_name, index)

        if self.__debounce is not None:
            self.after_cancel(self.__debounce)

        self.__debounce = self.after(
            100, lambda: self.tag_remove(tag_name, *tag_indices)
        )
