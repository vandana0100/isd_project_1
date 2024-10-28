"""
Description: Subject class for managing observers and notifying them of changes.
Author: Vandana Bhangu
"""

from .observer import Observer

class Subject:
    def __init__(self) -> None:
        """
        Initialize the Subject with an empty list of observers.
        """
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        """
        Add a new observer to the subject's list of observers.
        
        Args:
            observer (Observer): The observer to be added.
        """
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Remove an observer from the subject's list of observers.
        
        Args:
            observer (Observer): The observer to be removed.
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """
        Notify all registered observers of a state change.
        
        Args:
            message (str): The message to send to the observers.
        """
        for observer in self._observers:
            observer.update(message)
