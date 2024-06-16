from qualitag.interface.utils import Event, Observer


class TagEventsManager(Event):
    __observers: set[Observer] = set()
    __state = None

    @property
    def state(self) -> dict[str, str] | None:
        return self.__state

    def attach(self, observer: Observer):
        self.__observers.add(observer)

    def detach(self, observer: Observer):
        self.__observers.remove(observer)

    def notify(self):
        if self.__state is not None:
            for observer in self.__observers:
                observer.on_event(self)

    def generate_event(self, tag):
        """
        Generate an event for the given tag.

        Parameters
        ----------
        tag : TagView
            The tag to generate an event for.
        """
        if self.__state is None:
            self.__state = tag
            self.notify()
            self.__state = None
