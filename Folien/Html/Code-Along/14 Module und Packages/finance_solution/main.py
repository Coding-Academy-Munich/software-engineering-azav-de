from .analytics.budget import Budget
from .analytics.reporting import print_financial_report
from .expenses import Expense
from .income import Income


def record_income_and_expenses():
    incomes = [
        Income(5000, "Salary"),
        Income(200, "Interest"),
    ]
    expenses = [
        Expense(100, "Groceries"),
        Expense(150, "Utilities"),
        Expense(800, "Rent"),
        Expense(250, "Groceries"),
        Expense(300, "Entertainment"),
        Expense(100, "Groceries"),
    ]
    return incomes, expenses


def analyze_budget(expenses):
    budget = Budget(500)
    is_within_budget = budget.can_afford(expenses)
    print("Is within budget:", is_within_budget)


def main():
    incomes, expenses = record_income_and_expenses()
    analyze_budget(expenses)
    print()
    print_financial_report(incomes, expenses)


if __name__ == "__main__":
    main()
