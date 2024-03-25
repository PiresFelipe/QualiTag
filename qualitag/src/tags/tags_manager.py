from collections import defaultdict
from .tag import Tag


class TagManager:

    def __init__(self) -> None:

        self.__groups: dict[str, list[Tag]] = defaultdict(list)
        self.__tags: dict[str, Tag] = {}

    def _tag_exists(self, tag: Tag) -> bool:
        return tag in self.get_all_tags()

    def delete_group(self, group_name: str, delete_tags: bool = False) -> None:

        if group_name.lower() not in self.__groups.keys() or not isinstance(
            self.__groups[group_name], list
        ):
            raise KeyError(f"Group '{group_name}' does not exist or was not found.")

        if not delete_tags:
            for tag in self.__groups[group_name]:
                self.__tags[tag.name] = tag
        del self.__groups[group_name]

    def create_group(self, group_name: str) -> None:

        assert isinstance(group_name, str), "Invalid group name"
        if group_name.lower() in self.__groups.keys():
            raise ValueError(f"Group {group_name} already exists")

        self.__groups[group_name.lower()] = []

    def create_tag(
        self,
        tag_name: str,
        bg_color: str,
        fg_color: str,
        desc: str | None = None,
        group: str | None = None,
    ) -> None:

        new_tag = Tag(tag_name, bg_color, fg_color, desc)

        if self._tag_exists(new_tag):
            raise ValueError(f"Tag {tag_name} already exists")

        if group is not None:
            if group.lower() not in self.__groups.keys():
                self.create_group(group)
            self.__groups[group.lower()].append(new_tag)
        else:
            self.__tags[tag_name.lower()] = new_tag

    def get_all_tags(self) -> list[Tag]:
        tags = []

        tags.extend(list(self.__tags.values()))
        for group in self.__groups.values():
            tags.extend(group)

        return tags

    def get_all_groups(self) -> list[str]:
        return list(self.__groups.keys())
