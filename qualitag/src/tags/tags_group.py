# pylint: disable=missing-module-docstring
from attrs import define, field
from attrs.setters import frozen
from attrs.validators import instance_of, optional
from .tag import Tag


@define
class TagGroup:
    """
    Represents a group of tags with a name and optional description.

    Parameters:
    -----------
    name : str
        The name of the tag group.
    description : str, optional
        Description of the tag group.

    Methods:
    -----------
    __contains__(self, value: Tag) -> bool:
        Checks if a tag is present in the group.
    delete(self) -> List[Tag]:
        Deletes the tag group and returns its tags.
    add(self, item: Tag):
        Adds a tag to the group.
    remove(self, __value: Tag):
        Removes a tag from the group.
    get_tags(self):
        Retrieves the tags in the group.
    """
    name: str = field(eq=str.lower, validator=instance_of(str))
    __tags: list[Tag] = field(default=[], eq=False, init=False, on_setattr=frozen)
    description: str = field(default=None, eq=False, validator=optional(instance_of(str)))

    def __contains__(self, value: Tag) -> bool:
        if not isinstance(value, Tag):
            return False
        return value in self.__tags

    def delete(self) -> list[Tag]:
        """
        Deletes the tag group and returns its tags.

        Returns:
        --------
        List[Tag]
            The tags of the group before deletion.
        """
        return self.__tags

    def add(self, item: Tag):
        """
        Adds a tag to the group.

        Parameters:
        -----------
        item : Tag
            The tag to add.

        Raises:
        --------
        TypeError
            If the item is not an instance of Tag.
        ValueError
            If the tag already exists in the group.
        """
        if not isinstance(item, Tag):
            raise TypeError(f"Item of type {type(item)} can't be added to a TagGroup")

        if item in self.__tags:
            raise ValueError(
                f"Tag called `{item.name}` already exists in group {self.name}"
            )

        self.__tags.append(item)

    def remove(self, item: Tag):
        """
        Removes a tag from the group.

        Parameters:
        -----------
        item : Tag
            The tag to remove.

        Raises:
        --------
        TypeError
            If the value is not an instance of Tag.
        ValueError
            If the value is not present.
        """
        if not isinstance(item, Tag):
            raise TypeError(
                f"Element of type {type(item)} can not be a part of a TagGroup"
            )

        self.__tags.remove(item)

    def get_tags(self):
        """
        Retrieves the tags in the group.

        Returns:
        --------
        list[Tag]
            The list of tags in the group.
        """
        return self.__tags
