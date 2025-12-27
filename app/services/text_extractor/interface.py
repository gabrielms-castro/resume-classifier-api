from abc import ABC, abstractmethod

class TextExtractor(ABC):
    @abstractmethod
    def extract_text(self):
        raise NotImplementedError("This method should be implemented by subclasses")