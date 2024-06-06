from enum import Enum


class Term(Enum):
    SHORT = 60
    LARGE = 180

class Rate(Enum):
    MIN = 0.05
    MAX = 0.15

class Investment:
    def __init__(self) -> None:
        self._term = None
        self._interest_rate = None

    def __str__(self):
        return f"INVESTMENTE INFO:\nTerm: {self._term}, INTEREST RATE: {self._interest_rate}"

class InvestmentBuilder:

    def __init__(self) -> None:
        self._investment = Investment()

    def set_term(self, term: Term):
        self._investment._term = term.value
        return self

    def set_rate(self, rate: Rate):
        self._investment._interest_rate = rate.value
        return self

    def build(self):
        return self._investment

if __name__ == '__main__':
    investment_builder = InvestmentBuilder()
    investment = investment_builder.set_term(Term.LARGE).set_rate(Rate.MAX).build()
    print(investment)