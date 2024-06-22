from collections import defaultdict
from typing import TypeAlias, Union

TagsAssociation: TypeAlias = dict[str, list[tuple[int, int]]]


class Answer:

    def __init__(self, text: str) -> None:

        self.text = text
        self.__tags: TagsAssociation = defaultdict(list)

    def associate_tag(self, tag: str, start: int, end: int) -> None:
        self.__tags[tag].append((start, end))

    def dissociate_tag(self, tag: str, start: int, end: int) -> None:
        self.__tags[tag].remove((start, end))

    def get_all_tags(
        self, as_text: bool = False
    ) -> Union[TagsAssociation, dict[str, list[str]]]:
        if not as_text:
            return self.__tags

        tags: dict[str, list[str]] = {}
        for tag in self.__tags:
            tags[tag] = [self.text[start:end] for start, end in self.__tags[tag]]

        return tags
