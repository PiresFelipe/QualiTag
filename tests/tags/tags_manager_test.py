import pytest

from qualitag.src import Tag, TagsManager


@pytest.fixture(scope="class")
def tags_manager() -> TagsManager:
    return TagsManager()


def test_create_tag_success(tags_manager: TagsManager):
    tag = tags_manager.create_tag("Test", "#FFFFFF")
    assert isinstance(tag, Tag)
    assert tag.name == "Test"
    assert tag.color == "#FFFFFF"


def test_create_tag_already_exists(tags_manager: TagsManager):
    tags_manager.create_tag("Test", "#FFFFFF")
    with pytest.raises(ValueError):
        tags_manager.create_tag("Test", "#000000")


def test_tag_exists(tags_manager: TagsManager):
    tags_manager.create_tag("Test", "#FFFFFF")
    assert tags_manager.tag_exists("Test") is True
    assert tags_manager.tag_exists("NonExistent") is False


def test_get_tag(tags_manager: TagsManager):
    tags_manager.create_tag("Test", "#FFFFFF")
    tag = tags_manager.get_tag("Test")
    assert isinstance(tag, Tag)
    assert tag.name == "Test"


def test_get_tag_non_existent(tags_manager: TagsManager):
    with pytest.raises(ValueError):
        tags_manager.get_tag("NonExistent")


def test_delete_tag(tags_manager: TagsManager):
    tags_manager.create_tag("teste", "#FFFFFF")
    print(tags_manager.get_all_tags())
    tags_manager.delete_tag("teste")
    assert tags_manager.tag_exists("Test") is False


def test_delete_non_existent_tag(tags_manager: TagsManager):
    with pytest.raises(ValueError):
        tags_manager.delete_tag("NonExistent")


def test_get_all_tags(tags_manager: TagsManager):
    tags_manager.create_tag("Test1", "#FFFFFF")
    tags_manager.create_tag("Test2", "#000000")
    tags = tags_manager.get_all_tags()
    assert len(tags) == 2
    assert all(isinstance(tag, Tag) for tag in tags)
    assert all(tag.name in ["Test1", "Test2"] for tag in tags)
    assert all(tag.color in ["#FFFFFF", "#000000"] for tag in tags)
