from transformers import pipeline
from strategy_interface import QuestionAnsweringStrategy

class AlbertStrategy(QuestionAnsweringStrategy):
    def perform_qa(self, context, question):
        nlp = pipeline("question-answering", model="mfeb/albert-xxlarge-v2-squad2")
        return nlp(question=question, context=context)