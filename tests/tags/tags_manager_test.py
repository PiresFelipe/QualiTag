import pytest
from qualitag.src import TagsManager, Tag

@pytest.fixture
def tags_manager() -> TagsManager:
    return TagsManager()

def test_create_tag_success(tags_manager):
    tag = tags_manager.create_tag("Test", "#FFFFFF")
    assert isinstance(tag, Tag)
    assert tag.name == "Test"
    assert tag.color == "#FFFFFF"

def test_create_tag_already_exists(tags_manager):
    tags_manager.create_tag("Test", "#FFFFFF")
    with pytest.raises(ValueError):
        tags_manager.create_tag("Test", "#000000")

def test_tag_exists(tags_manager):
    tags_manager.create_tag("Test", "#FFFFFF")
    assert tags_manager.tag_exists("Test") is True
    assert tags_manager.tag_exists("NonExistent") is False

def test_get_tag(tags_manager):
    tags_manager.create_tag("Test", "#FFFFFF")
    tag = tags_manager.get_tag("Test")
    assert isinstance(tag, Tag)
    assert tag.name == "Test"

def test_get_tag_non_existent(tags_manager):
    with pytest.raises(ValueError):
        tags_manager.get_tag("NonExistent")

def test_delete_tag(tags_manager):
    tags_manager.create_tag("Test", "#FFFFFF")
    tags_manager.delete_tag("Test")
    assert tags_manager.tag_exists("Test") is False

def test_delete_non_existent_tag(tags_manager):
    with pytest.raises(ValueError):
        tags_manager.delete_tag("NonExistent")