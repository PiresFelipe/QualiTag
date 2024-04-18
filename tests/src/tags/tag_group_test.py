import pytest
from qualitag.src.tags import Tag, TagGroup

def test_tag_group_creation():
    tag_group = TagGroup("TestGroup", "Test group description")

    assert tag_group.name == "TestGroup"
    assert tag_group.description == "Test group description"
    assert tag_group.get_tags() == []

def test_tag_group_add_tag():
    tag1 = Tag("Test1", "red", "white", "Test Description1")
    tag_group = TagGroup("TestGroup")

    tag_group.add(tag1)
    assert tag1 in tag_group.get_tags()
    pytest.raises(ValueError, tag_group.add, tag1)

def test_tag_group_remove_tag():
    tag1 = Tag("Test1", "red", "white", "Test Description1")
    tag2 = Tag("Test2", "blue", "black", "Test Description2")
    tag_group = TagGroup("TestGroup")
    
    tag_group.add(tag1)
    tag_group.add(tag2)

    tag_group.remove(tag1)
    assert tag1 not in tag_group.get_tags()
    pytest.raises(ValueError, tag_group.remove, tag1)
    