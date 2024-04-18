from attrs import define, field
from attrs.validators import instance_of, optional
from src.tags import Tag


@define
class TagGroup:

    name: str = field(validator=instance_of(str), eq=str.lower)
    description: str | None = field(
        default=None, validator=optional(instance_of(str)), eq=False
    )
    tags: list[Tag] = field(factory=list, eq=False)
