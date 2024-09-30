class TagsCounter:
    def __init__(self):
        self.__counts: dict[str, int] = {}

    def increment(self, tag: str):
        tag = tag.lower()
        if tag not in self.__counts:
            self.__counts[tag] = 0
        self.__counts[tag] += 1

    def decrement(self, tag: str):
        tag = tag.lower()
        if tag in self.__counts:
            self.__counts[tag] -= 1
            if self.__counts[tag] == 0:
                del self.__counts[tag]

    def get_all(self):
        return self.__counts

    def get_count(self, tag: str):
        tag = tag.lower()
        return self.__counts.get(tag, 0)

    def delete(self, tag: str):
        tag = tag.lower()
        if tag in self.__counts:
            del self.__counts[tag]

    def __str__(self): # pragma: no cover
        return str(self.__counts)
