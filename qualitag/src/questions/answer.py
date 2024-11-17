from collections import defaultdict
from typing import TypeAlias, Union

TagsAssociation: TypeAlias = dict[str, set[tuple[int, int]]]


class Answer:
    """
    A class to represent an Answer with text and associated tags.
    """
    def __init__(self, text: str) -> None:

        self.text = text
        self.__tags: TagsAssociation = defaultdict(set)

    @property
    def tags(self) -> TagsAssociation:
        """
        The tags associated with the answer.
        """
        return self.__tags

    def delete_tag(self, tag: str) -> None:
        """
        Deletes a tag from the internal tags dictionary.
        Args:
            tag (str): The tag to be deleted.
        Raises:
            KeyError: If the tag does not exist, the exception is caught and passed.
        """
        try:
            del self.__tags[tag]
        except KeyError:
            pass

    def associate_tag(self, tag: str, start: int, end: int) -> bool:
        """
        Associates a tag with a specified range (start, end).
        Args:
            tag (str): The tag to be associated.
            start (int): The starting index of the range.
            end (int): The ending index of the range.
        Returns:
            bool: True if the tag was successfully associated with the range (i.e., the range was not already associated with the tag), False otherwise.
        """
        _len = len(self.__tags[tag])
        self.__tags[tag].add((start, end))
        return len(self.__tags[tag]) != _len

    def dissociate_tag(self, tag: str, start: int, end: int) -> None:
        """
        Dissociates a tag from a specified range.
        This method removes the association of a given tag with a specified range 
        defined by the start and end positions.
        Args:
            tag (str): The tag to dissociate.
            start (int): The starting position of the range.
            end (int): The ending position of the range.
        """
        
        self.__tags[tag].remove((start, end))

    def get_all_tags(
        self, as_text: bool = False
    ) -> Union[TagsAssociation, dict[str, list[str]]]:
        """
        Retrieve all tags associated with the text.
        Args:
            as_text (bool): If True, returns the tags as a dictionary with tag names as keys
                            and lists of corresponding text segments as values. If False,
                            returns the tags in their original format.
        Returns:
            Union[TagsAssociation, dict[str, list[str]]]: The tags in their original format or as a dictionary with text segments.
        """
        if not as_text:
            return self.__tags

        tags: dict[str, list[str]] = {}
        for tag in self.__tags:
            tags[tag] = [self.text[start:end] for start, end in self.__tags[tag]]

        return tags

    def get_tag_text(self, tag: str) -> list[str]:
        """
        Retrieve the text segments associated with a specific tag.
        Args:
            tag (str): The tag for which to retrieve the text segments.
        Returns:
            list[str]: A list of text segments corresponding to the specified tag.
        """
        return [self.text[start:end] for start, end in self.__tags[tag]]
