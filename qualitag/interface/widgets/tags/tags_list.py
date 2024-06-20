from qualitag.src import TagsManager, Tag
from qualitag.interface.widgets.tags.tag_views import TagView
from qualitag.interface.widgets.tags.tags_events import TagEventsManager
from customtkinter import CTkScrollableFrame, CTkFont

class TagsList(CTkScrollableFrame):

    def __init__(self, *args, manager: TagsManager, events: TagEventsManager, **kwargs):
        super().__init__(*args, **kwargs)

        self.__manager = manager
        self.__events = events
        self.__views_list: list[Tag] = []
        
        self.configure(
            label_text = "Tags",
            label_font = CTkFont(weight="bold")
        )
        
        self.update_tags()
        
    def update_tags(self):
        self.__views_list = []
        for tag in self.__manager.get_all_tags(sort=True):
            view = TagView(self, tag=tag, events_manager=self.__events)
            view.pack(padx=5, pady=5)
        