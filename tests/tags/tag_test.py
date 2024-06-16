import pytest
from qualitag.src import Tag


def test_tag_initialization():
    tag = Tag(name="Test", color="Blue", description="A test tag")
    assert tag.name == "Test"
    assert tag.color == "Blue"
    assert tag.description == "A test tag"


def test_case_insensitive_comparison():
    tag1 = Tag(name="Test", color="Blue")
    tag2 = Tag(name="test", color="Blue")
    assert tag1 == tag2


def test_invalid_name_type():
    with pytest.raises(TypeError):
        Tag(name=123, color="Blue")


def test_invalid_color_type():
    with pytest.raises(TypeError):
        Tag(name="Test", color=123)


def test_invalid_description_type():
    with pytest.raises(TypeError):
        Tag(name="Test", color="Blue", description=123)


def test_optional_description():
    tag = Tag(name="Test", color="Blue")
    assert tag.description is None


def test_tag_change_values():
    tag = Tag(
        name="Test", color="red", description="Test Description"
    )

    tag.name = "Changed"
    tag.description = None

    assert tag.name == "Changed"
    assert tag.color == "red"
    assert tag.description is None

    with pytest.raises(TypeError):
        tag.name = 0

    with pytest.raises(TypeError):
        tag.description = 0
