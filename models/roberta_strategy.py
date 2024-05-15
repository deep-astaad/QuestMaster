from transformers import pipeline
from strategy_interface import QuestionAnsweringStrategy

class RoBERTaStrategy(QuestionAnsweringStrategy):
    def perform_qa(self, context, question):
        nlp = pipeline("question-answering", model="deepset/roberta-base-squad2")
        return nlp(question=question, context=context)