from transformers import pipeline
from strategy_interface import QuestionAnsweringStrategy

class XLNetStrategy(QuestionAnsweringStrategy):
    def perform_qa(self, context, question):
        nlp = pipeline("question-answering", model="xlnet-base-cased")
        return nlp(question=question, context=context)