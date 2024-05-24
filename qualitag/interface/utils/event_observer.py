from __future__ import annotations
from abc import ABC, abstractmethod

class Event(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
            """
            Attach an observer to the subject.

            Parameters
            ----------
            observer : Observer
                The observer to be attached.

            Returns
            -------
            None
            """
            pass
    
    @abstractmethod
    def detach(self, observer: Observer):
            """
            Detaches an observer from the subject.

            Parameters
            ----------
            observer : Observer
                The observer to be detached.

            Returns
            -------
            None
            """
            pass
    
    @abstractmethod
    def notify(self):
            """
            Notify the observer about an event.

            This method is called to notify the observer about an event that has occurred.
            Implementations of this method should handle the event accordingly.

            Parameters:
                self (EventObserver): The current instance of the EventObserver class.

            Returns:
                None
            """
            pass

class Observer(ABC):
    @abstractmethod
    def on_event(self, event: Event):
        pass
    