from attrs import define, field
from attrs.validators import instance_of, optional
from . import Tag


@define
class TagGroup:

    name: str = field(validator=instance_of(str), eq=str.lower)
    description: str | None = field(
        default=None, validator=optional(instance_of(str)), eq=False
    )
    __tags: list[Tag] = field(factory=list, eq=False)

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
        """
        if not isinstance(tag, Tag):
            raise ValueError("tag must be an instance of Tag")
        self.__tags.append(tag)

    def remove(self, tag: Tag | str):
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

            Returns:
                list[Tag]: The list of tags in the tag group.
            """
            return self.__tags
