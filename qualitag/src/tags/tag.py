from attr import define, field
from attr.validators import instance_of, optional


@define
class Tag:

    name: str = field(validator=instance_of(str), eq=str.lower)
    bg_color: str = field(validator=instance_of(str), eq=False)
    fg_color: str = field(validator=instance_of(str), eq=False)
    description: str | None = field(
        default=None, validator=optional(instance_of(str)), eq=False
    )
