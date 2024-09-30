import pytest
from qualitag.src.questions import Answer  # Import the Answer class

# TagsAssociation is a type alias for dict[str, set[tuple[int, int]]]
TagsAssociation = dict[str, set[tuple[int, int]]]


def test_answer_initialization():
    answer_text = "This is an answer"
    answer = Answer(answer_text)

    assert answer.text == answer_text
    assert isinstance(answer.tags, dict)
    assert answer.tags == {}  # tags should be an empty dictionary initially


def test_associate_tag():
    answer = Answer("This is an answer")

    # Associate a tag with a range
    result = answer.associate_tag("important", 0, 4)

    assert result == True  # First association should return True (new entry)
    assert "important" in answer.tags
    assert answer.tags["important"] == {(0, 4)}

    # Associate the same tag and range again, should return False (no change)
    result = answer.associate_tag("important", 0, 4)
    assert result == False


def test_dissociate_tag():
    answer = Answer("This is an answer")

    # Associate and then dissociate a tag
    answer.associate_tag("important", 0, 4)
    answer.dissociate_tag("important", 0, 4)

    assert "important" in answer.tags
    assert answer.tags["important"] == set()  # Tag still exists but is empty


def test_delete_tag():
    answer = Answer("This is an answer")

    # Associate a tag and then delete it
    answer.associate_tag("important", 0, 4)
    answer.delete_tag("important")

    assert "important" not in answer.tags  # Tag should be completely removed


def test_delete_nonexistent_tag():
    answer = Answer("This is an answer")

    # Try to delete a tag that doesn't exist (should not raise an error)
    answer.delete_tag("nonexistent")

    assert "nonexistent" not in answer.tags  # Tag should not exist


def test_get_all_tags():
    answer = Answer("This is an answer")

    # Associate a couple of tags
    answer.associate_tag("important", 0, 4)
    answer.associate_tag("keyword", 5, 7)

    # Get all tags as a dict
    tags = answer.get_all_tags()
    assert tags == {
        "important": {(0, 4)},
        "keyword": {(5, 7)},
    }


def test_get_all_tags_as_text():
    answer = Answer("This is an answer")

    # Associate a couple of tags
    answer.associate_tag("important", 0, 4)  # "This"
    answer.associate_tag("keyword", 5, 7)  # "is"

    # Get all tags as text
    tags_as_text = answer.get_all_tags(as_text=True)

    assert tags_as_text == {
        "important": ["This"],
        "keyword": ["is"],
    }


def test_get_tag_text():
    answer = Answer("This is an answer")

    # Associate tags and get specific tag text
    answer.associate_tag("important", 0, 4)  # "This"
    answer.associate_tag("important", 8, 10)  # "an"

    tag_text = answer.get_tag_text("important")

    assert tag_text == ["an", "This"]


def test_dissociate_nonexistent_tag():
    answer = Answer("This is an answer")

    # Try dissociating a tag that doesn't exist, should raise no error
    with pytest.raises(KeyError):
        answer.dissociate_tag("nonexistent", 0, 4)


def test_dissociate_nonexistent_range_from_tag():
    answer = Answer("This is an answer")

    # Associate a tag
    answer.associate_tag("important", 0, 4)

    # Try dissociating a range that doesn't exist within the tag
    with pytest.raises(KeyError):
        answer.dissociate_tag("important", 5, 7)
