# finance/income.py

from dataclasses import dataclass

@dataclass
class Income:
    amount: float
    source: str


def summarize_incomes(incomes: list[Income]) -> dict[str, float]:
    summary: dict[str, float] = {}
    for income in incomes:
        source = income.source
        summary[source] = summary.get(source, 0) + income.amount
    return summary


def total_income(incomes: list[Income]) -> float:
    return sum(income.amount for income in incomes)
