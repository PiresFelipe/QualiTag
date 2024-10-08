from abc import ABC, abstractmethod
from typing import Union

from attrs import define, field
from attrs.validators import in_

from qualitag.src import Tag

EVENT_TYPES = ["created", "clicked", "deleted"]


@define
class Event:
    """
    Represents an event.

    Attributes
    ----------
    event_type : Literal["created", "clicked"]
        The type of the event.
    tag : TagView | Tag
        The associated tag.
    """

    event_type: str = field(validator=in_(EVENT_TYPES))
    tag: Union["TagView", Tag] = field()


class Observer(ABC):
    @abstractmethod
    def on_event(self, event: Event):
        pass
