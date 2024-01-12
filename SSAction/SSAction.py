from abc import ABC, abstractmethod

class SSAction(ABC):
    @abstractmethod
    def get_ss(self, ss_object):
        pass

    def action(self):
        pass
