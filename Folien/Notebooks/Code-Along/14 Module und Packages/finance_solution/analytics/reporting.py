# finance/analytics/reports.py


from ..income import Income, summarize_incomes, total_income
from ..expenses import Expense, summarize_expenses, total_expenses


def print_financial_report(incomes: list[Income], expenses: list[Expense]) -> None:

    print("Financial Report")
    print("-----------------")

    print_income_summary(incomes)
    print_expense_summary(expenses)
    print_totals(incomes, expenses)


def print_income_summary(incomes):
    print("Income Summary:")
    income_summary = summarize_incomes(incomes)
    for source, amount in income_summary.items():
        print(f"{source + ':':<15} ${amount:8.2f}")


def print_expense_summary(expenses):
    print("\nExpense Summary:")
    expense_summary = summarize_expenses(expenses)
    for category, amount in expense_summary.items():
        print(f"{category + ':':<15} ${amount:8.2f}")


def print_totals(incomes, expenses):
    total_inc = total_income(incomes)
    total_exp = total_expenses(expenses)

    print(f"\nTotal Income:   ${total_inc:8.2f}")
    print(f"Total Expenses: ${total_exp:8.2f}")
    print(f"Net Income:     ${total_inc - total_exp:8.2f}")
