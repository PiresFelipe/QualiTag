from typing import Union
from qualitag.src import Tag
from abc import ABC, abstractmethod
from attrs import define, field
from attrs.validators import in_

EVENT_TYPES = ["created", "clicked"]


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
