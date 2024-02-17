# pylint: skip-file
import pytest
from qualitag.src.tags import Tag


def test_tag_creation():
    tag = Tag(
        name="Test", bg_color="red", fg_color="white", description="Test Description"
    )
    assert tag.name == "Test"
    assert tag.bg_color == "red"
    assert tag.fg_color == "white"
    assert tag.description == "Test Description"


def test_tag_default_description():
    tag = Tag(name="Test", bg_color="red", fg_color="white")
    assert tag.description is None


def test_tag_comparations():
    tag_a = Tag(name="Tag1", bg_color="red", fg_color="white", description="Desc")
    tag_b = Tag(name="tag1", bg_color="red", fg_color="white")
    tag_c = Tag(name="Tag2", bg_color="red", fg_color="yellow")
    tag_d = Tag(name="Tag2", bg_color="blue", fg_color="white")

    assert tag_a == tag_b
    assert tag_c == tag_d
    assert not tag_a == tag_c
    assert not tag_b == tag_d


def test_tag_type_init():
    with pytest.raises(TypeError):
        tag = Tag(1, "red", "blue", "description")
    with pytest.raises(TypeError):
        tag = Tag("Test", 2, "blue", "description")
    with pytest.raises(TypeError):
        tag = Tag("Test", "red", 3, "description")
    with pytest.raises(TypeError):
        tag = Tag("Test", "red", "blue", 4)


def test_tag_change_values():
    tag = Tag(
        name="Test", bg_color="red", fg_color="white", description="Test Description"
    )

    tag.name = "Changed"
    tag.bg_color, tag.fg_color = tag.fg_color, tag.bg_color
    tag.description = None

    assert tag.name == "Changed"
    assert tag.bg_color == "white"
    assert tag.fg_color == "red"
    assert tag.description is None

    with pytest.raises(TypeError):
        tag.name = 0

    with pytest.raises(TypeError):
        tag.description = 0
