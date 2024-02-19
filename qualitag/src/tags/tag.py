# pylint: disable=missing-module-docstring
from attrs import define, field
from attrs.validators import instance_of, optional


@define
class Tag:
    """
    A class representing a tag with its associated properties.

    Parameters
    ----------
    name : str
        The name of the tag.
    bg_color : str
        The background color associated with the tag.
    fg_color : str
        The foreground color associated with the tag.
    description : str or None, optional
        The description of the tag, if available.

    Notes
    -----
    - This class considers another tag class equal just \\
    by the `name` parameter, and is not case-sensitive.

    Examples
    --------
    >>> tag1 = Tag(name="important", bg_color="red",
        fg_color="white", description="This tag signifies importance.")
    >>> tag2 = Tag(name="low priority", bg_color="gray", fg_color="black")
    """

    name: str = field(validator=instance_of(str), eq=str.lower)
    bg_color: str = field(validator=instance_of(str), eq=False)
    fg_color: str = field(validator=instance_of(str), eq=False)
    description: str | None = field(
        default=None, validator=optional(instance_of(str)), eq=False
    )
