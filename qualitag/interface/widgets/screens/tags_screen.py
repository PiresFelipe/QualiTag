from typing import Callable

import customtkinter as ctk

from qualitag.src import TagsManager

from ...utils import fonts
from ...utils.tags_events import TagEventsManager
from ..tags import TagDescriptor


class TagsScreen(ctk.CTkFrame):

    def __init__(
        self,
        *args,
        tags_manager: TagsManager,
        create_fn: Callable,
        event_manager: TagEventsManager,
        **kwargs
    ):
        super().__init__(*args, **kwargs)

        title = ctk.CTkFont(**fonts["h1"])
        subtitle = ctk.CTkFont(**fonts["h3"])

        ctk.CTkLabel(self, text="Tags", font=title, anchor="w").pack(
            pady=[10, 0], padx=30, fill="x"
        )
        ctk.CTkLabel(
            self,
            text="Visualize e gerencie todas as suas tags",
            anchor="w",
            font=subtitle,
        ).pack(pady=10, padx=30, fill="x")

        self.tags_counter = TagDescriptor(
            self,
            tags_manager=tags_manager,
            events_manager=event_manager,
            fg_color="transparent",
        )
        self.tags_counter.pack(pady=10, fill="both", expand=True)
        event_manager.attach(self.tags_counter)

        ctk.CTkButton(self, text="Criar nova tag", command=create_fn).pack(
            pady=10, padx=30
        )
