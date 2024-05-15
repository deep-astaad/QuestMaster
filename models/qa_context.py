class QAContext:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def perform_qa(self, context, question):
        return self._strategy.perform_qa(context, question)