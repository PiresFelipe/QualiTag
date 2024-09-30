import pytest
from qualitag.src.tags import TagsManager, TagsCounter

@pytest.fixture
def tags_manager():
    return TagsManager()

def test_tags_counter_created(tags_manager: TagsManager):
    assert isinstance(tags_manager.counter, TagsCounter)
    
def test_tags_counter_increment(tags_manager: TagsManager):
    tags_manager.counter.increment("Test")
    assert tags_manager.counter.get_count("Test") == 1
    
def test_tags_counter_decrement(tags_manager: TagsManager):
    tags_manager.counter.increment("Test")
    tags_manager.counter.decrement("Test")
    assert tags_manager.counter.get_count("Test") == 0
    
def test_tags_counter_delete(tags_manager: TagsManager):
    tags_manager.counter.increment("Test")
    tags_manager.counter.increment("Test")
    tags_manager.counter.delete("Test")
    assert tags_manager.counter.get_count("Test") == 0
    
def test_get_all_tags(tags_manager: TagsManager):
    tags_manager.counter.increment("Test")
    tags = tags_manager.counter.get_all()
    assert tags == {"test": 1}
