from qualitag.interface.utils.event_observer import Observer
from qualitag.src import TagsManager
from qualitag.interface.widgets.tags.tag_views import TagView
from qualitag.interface.utils.tags_events import TagEventsManager
from customtkinter import CTkScrollableFrame, CTkFont


class TagsList(CTkScrollableFrame, Observer):

    def __init__(self, *args, manager: TagsManager, events: TagEventsManager, **kwargs):
        super().__init__(*args, **kwargs)

        self.__manager = manager
        self.__events = events
        self.__views_list: list[TagView] = []

        self.configure(label_text="Tags", label_font=CTkFont(weight="bold"))

        self.__events.attach(self)
        self.update_tags()

    def update_tags(self):
        for _ in range(len(self.__views_list)):
            tag_view = self.__views_list.pop()
            tag_view.destroy()
            
        for tag in self.__manager.get_all_tags(sort=True):
            view = TagView(self, tag=tag, events_manager=self.__events)
            view.pack(padx=5, pady=5)
            self.__views_list.append(view)

    def on_event(self, event):
        if event.event_type == "created":
            self.update_tags()

            
    
