from .event_observer import Event, Observer
from .tags_events import TagEventsManager

font_family = "Roboto"

fonts = {
    "h1": {"family": font_family, "size": 24, "weight": "bold"},
    "h2": {"family": font_family, "size": 18, "weight": "bold"},
    "h3": {"family": font_family, "size": 16, "weight": "bold"},
    "body": {"family": font_family, "size": 16},
    "small": {"family": font_family, "size": 14},
}

__all__ = ["Event", "Observer", "TagEventsManager"]
