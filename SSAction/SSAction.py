from abc import ABC, abstractmethod


class SSAction(ABC):

    @abstractmethod
    def action(self):
        pass
