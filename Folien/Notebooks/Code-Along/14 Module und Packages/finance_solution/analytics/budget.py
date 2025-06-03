# finance/analytics/budget.py

from dataclasses import dataclass
from ..expenses import Expense, total_expenses


@dataclass
class Budget:
    limit: float

    def can_afford(self, expenses: list[Expense]) -> bool:
        total_expense = total_expenses(expenses)
        return total_expense <= self.limit
