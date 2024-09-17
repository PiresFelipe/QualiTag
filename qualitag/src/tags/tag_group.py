from typing import Optional, Union

from attrs import define, field
from attrs.validators import instance_of, optional

from . import Tag


@define
class TagGroup:
    """
    Represents a group of tags.

    Attributes
    ----------
    name : str
        The name of the tag group.
    description : str or None, optional
        The description of the tag group.

    Methods
    -------
    add(tag)
        Add a tag to the tag group.
    remove(tag)
        Remove a tag from the tag group.
    get_tags()
        Get the list of tags in the tag group.
    """

    name: str = field(validator=instance_of(str), eq=str.lower)
    description: Optional[str] = field(
        default=None, validator=optional(instance_of(str)), eq=False
    )
    __tags: list[Tag] = field(factory=list, eq=False, init=False)

    def add(self, tag: Tag):
        """
        Add a tag to the tag group.

        Parameters
        ----------
        tag : Tag
            The tag to be added to the tag group.

        Raises
        ------
        ValueError
            If the provided tag is not an instance of Tag.
            Or if the tag is already present in the tag group.
        """
        if not isinstance(tag, Tag):
            raise ValueError("tag must be an instance of Tag")
        if tag in self.__tags:
            raise ValueError("Tag already present in the tag group")

        self.__tags.append(tag)

    def remove(self, tag: Union[Tag, str]):
        """
        Remove a tag from the tag group.

        Parameters
        ----------
        tag : Tag or str
            The tag to be removed. It can be either an instance of the Tag class or a string.

        Raises
        ------
        ValueError
            If the tag is not an instance of Tag or a string.
            Or if value is not present in the tag group.
        """
        if not isinstance(tag, (Tag, str)):
            raise ValueError("tag must be an instance of Tag or a string")

        if isinstance(tag, str):
            tag = Tag(tag, "", "")

        self.__tags.remove(tag)

    def get_tags(self) -> list[Tag]:
        """
        Get the list of tags in the tag group.
        """
        return self.__tags.copy()
