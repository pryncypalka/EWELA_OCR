from abc import ABC, abstractmethod


class Window(ABC):
    @abstractmethod
    def close_window(self, event):
        pass
