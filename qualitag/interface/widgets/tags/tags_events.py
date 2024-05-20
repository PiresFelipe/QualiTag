from utils import Event, Observer

class TagEvent(Event):
    __observers: set[Observer] = set()
    __state: dict[str, str] | None = None
    
    def attach(self, observer: Observer):
        self.__observers.add(observer)
    
    def detach(self, observer: Observer):
        self.__observers.remove(observer)
    
    def notify(self):
        if self.__state is not None:
            for observer in self.__observers:
                observer.on_event(self.__state)
    
    def generate_event(self, tag):
        """
        Generate an event for the given tag.

        Parameters
        ----------
        tag : str
            The tag to generate an event for.
        """
        if self.__state is not None:
            self.__state = tag
            self.notify()
            self.__state = None