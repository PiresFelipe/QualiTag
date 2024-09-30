from collections import defaultdict
from typing import Optional, Union

from .tag import Tag
from .tags_counter import TagsCounter

# from .tag_group import TagGroup    ## future usage


class TagsManager:

    def __init__(self) -> None:

        # self.__groups: list[TagGroup] = [] # future usage
        self.__tags: dict[str, Tag] = {}
        self.__counter = TagsCounter()

    @property
    def counter(self) -> TagsCounter:
        return self.__counter

    def create_tag(
        self, name: str, color: str, description: Optional[str] = None
    ) -> Tag:
        """
        Creates a new tag.

        Returns:
        ---
            Tag: The newly created tag.

        Raises:
        ---
            ValueError: If a tag with the given name already exists.
        """
        if self.tag_exists(name):
            raise ValueError(f"Tag with name {name} already exists")

        self.__tags[name.lower()] = Tag(name=name, color=color, description=description)

        return Tag(name=name, color=color, description=description)

    def tag_exists(self, tag_name: str) -> bool:
        """
        Checks if a tag with the given name exists in the tags manager.

        Args:
        ---
            tag_name (str): The name of the tag to check.

        Returns:
        ---
            bool: True if the tag exists, False otherwise.
        """
        return tag_name.lower() in self.__tags

    def get_tag(self, tag_name: str) -> Tag:
        """
        Gets the tag with the given name.

        Args:
        ---
            tag_name (str): The name of the tag to get.

        Returns:
        ---
            Tag: The tag with the given name.
        """
        try:
            return self.__tags[tag_name.lower()]
        except KeyError as exc:
            raise ValueError(f"Tag with name {tag_name} does not exist") from exc

    def delete_tag(self, tag: Union[str, Tag]) -> None:
        """
        Deletes the tag with the given name.

        Args:
        ---
            tag (str | Tag): The name of the tag to delete or the tag itself.
        """
        if isinstance(tag, str):
            tag_name = tag
        else:
            tag_name = tag.name

        try:
            del self.__tags[tag_name.lower()]
            self.__counter.delete(tag_name)
        except KeyError as exc:
            raise ValueError(f"Tag with name {tag_name} does not exist") from exc

    def get_all_tags(self, sort: bool = False) -> list[Tag]:
        """
        Gets all the tags in the tags manager.

        Returns:
        ---
            list[Tag]: The list of all tags in the tags manager.
        """
        if sort:
            return sorted(self.__tags.values(), key=lambda tag: tag.name)
        return list(self.__tags.values())
