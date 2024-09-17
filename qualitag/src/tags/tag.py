# pylint: disable=missing-module-docstring
from typing import Optional

from attrs import define, field
from attrs.validators import instance_of, optional


@define
class Tag:
    """
    A class to represent a Tag with a name, color, and an optional description.

    Attributes
    ----------
    name : str
        The name of the tag. Comparison is case-insensitive.
    color : str
        The color of the tag.
    description : str, optional
        An optional description of the tag. Defaults to None.
    """

    name: str = field(validator=instance_of(str), eq=str.lower)
    color: str = field(validator=instance_of(str))
    description: Optional[str] = field(
        default=None, validator=optional(instance_of(str)), eq=False
    )
