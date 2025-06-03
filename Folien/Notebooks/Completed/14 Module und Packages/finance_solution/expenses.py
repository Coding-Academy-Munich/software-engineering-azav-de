# finance/expenses.py

from dataclasses import dataclass

@dataclass
class Expense:
    amount: float
    category: str


def summarize_expenses(expenses: list[Expense]) -> dict[str, float]:
    summary: dict[str, float] = {}
    for expense in expenses:
        category = expense.category
        summary[category] = summary.get(category, 0) + expense.amount
    return summary


def total_expenses(expenses: list[Expense]) -> float:
    return sum(expense.amount for expense in expenses)
