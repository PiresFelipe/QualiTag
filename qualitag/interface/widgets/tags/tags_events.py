from typing import Literal, Union
from qualitag.src import Tag
from qualitag.interface.utils import Event, Observer
from qualitag.interface.widgets.tags.tag_views import TagView


class TagEventsManager:
    __observers: set[Observer] = set()

    def attach(self, observer: Observer):
        """
        Attach an observer to the subject.

        Parameters
        ----------
        observer : Observer
            The observer to be attached.
        """
        self.__observers.add(observer)

    def detach(self, observer: Observer):
        """
        Detaches an observer from the subject.

        Parameters
        ----------
        observer : Observer
            The observer to be detached.
        """
        self.__observers.remove(observer)

    def notify(self, event: Event):
        for observer in self.__observers:
            observer.on_event(event)

    def generate_event(
        self, event_type: Literal["created", "clicked"], tag: Union[TagView, Tag]
    ):
        """
        Generate an event for the given tag.

        Parameters
        ----------
        tag : TagView
            The tag to generate an event for.
        """
        event = Event(event_type=event_type, tag=tag)
        self.notify(event)
