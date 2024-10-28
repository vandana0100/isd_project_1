"""
Description: Observer interface for notifying observers of changes in the subject.
Author: Vandana Bhangu
"""

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        """
        This method will be called to notify the observer of changes in the subject.

        :param message: The message to be sent to the observer.
        """
        pass
