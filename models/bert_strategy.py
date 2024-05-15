from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
from strategy_interface import QuestionAnsweringStrategy

class BertStrategy(QuestionAnsweringStrategy):
    def perform_qa(self, context, question):
        model_name = "deepset/bert-large-uncased-whole-word-masking-squad2"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForQuestionAnswering.from_pretrained(model_name)
        nlp = pipeline("question-answering", model=model, tokenizer=tokenizer)
        return nlp(question=question, context=context)