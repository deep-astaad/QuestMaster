from transformers import pipeline
from strategy_interface import QuestionAnsweringStrategy

class DistilBERTStrategy(QuestionAnsweringStrategy):
    def perform_qa(self, context, question):
        nlp = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
        return nlp(question=question, context=context)