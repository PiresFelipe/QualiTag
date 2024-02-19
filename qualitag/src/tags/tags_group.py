# pylint: disable=missing-module-docstring
from attrs import define, field
from attrs.setters import frozen
from attrs.validators import instance_of, optional
from .tag import Tag


@define
class TagGroup:

    name: str = field(eq=str.lower, validator=instance_of(str))
    __tags: list[Tag] = field(default=[], eq=False, init=False, on_setattr=frozen)
    description: str = field(default=None, validator=optional(instance_of(str)))

    def __contains__(self, value: Tag) -> bool:
        if not isinstance(value, Tag):
            return False
        return value in self.__tags

    def __del__(self) -> list[Tag]:
        return self.__tags

    def add(self, item: Tag):
        if not isinstance(item, Tag):
            raise TypeError(f"Item of type {type(item)} can't be added to a TagGroup")

        if item in self.__tags:
            raise ValueError(
                f"Tag called `{item.name}` already exists in group {self.name}"
            )

        self.__tags.append(item)

    def remove(self, __value: Tag):
        if not isinstance(__value, Tag):
            raise TypeError(
                f"Element of type {type(__value)} can not be a part of a TagGroup"
            )

        self.__tags.remove(__value)

    def get_tags(self):
        return self.__tags
