# pylint: skip-file
# type: ignore
import pytest
from qualitag.src.tags import Tag, TagGroup


@pytest.fixture
def tag():
    return Tag("Test1", "red", "white", "Description1")


@pytest.fixture
def tag_group():
    return TagGroup("Test", "Description")


def test_group_creation(tag_group):
    assert tag_group.name == "Test"
    assert tag_group.description == "Description"
    assert tag_group.get_tags() == []


def test_name_comparisons(tag_group):
    group2 = TagGroup("test")
    group3 = TagGroup("Different", "Description")
    
    assert tag_group == tag_group
    assert tag_group == group2
    assert not tag_group == group3
    


def test_add_tag(tag_group, tag):
    tag_group.add(tag)
    assert tag_group.get_tags() == [tag]


def test_remove_tag(tag_group, tag):
    tag_group.remove(tag)
    assert tag_group.get_tags() == []


def test_contains(tag_group, tag):
    tag_group.add(tag)
    assert tag in tag_group
    assert Tag("Not a tag", "blue", "black") not in tag_group


def test_add_existing_tag(tag_group, tag):
    with pytest.raises(ValueError):
        tag_group.add(tag)


def test_add_invalid_tag(tag_group):
    with pytest.raises(TypeError):
        tag_group.add("Invalid Tag")


def test_remove_invalid_tag(tag_group):
    with pytest.raises(TypeError):
        tag_group.remove("Invalid Tag")


def test_delete(tag_group, tag):
    deleted_tags = tag_group.delete()
    assert deleted_tags == [tag]
