from abc import ABC, abstractmethod

class command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def getCommand(self):
        pass