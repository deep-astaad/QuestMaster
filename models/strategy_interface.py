from abc import ABC, abstractmethod

class QuestionAnsweringStrategy(ABC):
    @abstractmethod
    def perform_qa(self, context, question):
        pass