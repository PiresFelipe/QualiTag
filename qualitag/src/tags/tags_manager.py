from .tag import Tag
from .tag_group import TagGroup


class TagManager:

    def __init__(self) -> None:

        self.__groups: TagGroup = TagGroup()
        self.__tags: dict[str, Tag] = {}

    def create_tag(self) -> Tag:
        ...
    
