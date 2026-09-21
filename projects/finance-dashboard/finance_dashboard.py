import csv
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / 'data' / 'finance_data.csv'


def load_rows():
    with open(DATA_FILE, newline='') as file:
        return list(csv.DictReader(file))


def summarize(rows):
    total_income = 0.0
    total_expense = 0.0
    category_income = defaultdict(float)
    category_expense = defaultdict(float)

    for row in rows:
        category = row['Category']
        income = float(row['Income'])
        expense = float(row['Expense'])

        total_income += income
        total_expense += expense
        category_income[category] += income
        category_expense[category] += expense

    return {
        'total_income': total_income,
        'total_expense': total_expense,
        'profit': total_income - total_expense,
        'category_income': dict(category_income),
        'category_expense': dict(category_expense),
    }


def main():
    rows = load_rows()
    summary = summarize(rows)

    print('=== Finance Dashboard ===')
    print(f'Total Income: ${summary["total_income"]:,.2f}')
    print(f'Total Expense: ${summary["total_expense"]:,.2f}')
    print(f'Net Profit: ${summary["profit"]:,.2f}')

    print('\nIncome by Category:')
    for category, value in sorted(summary['category_income'].items(), key=lambda x: x[1], reverse=True):
        print(f'- {category}: ${value:,.2f}')

    print('\nExpense by Category:')
    for category, value in sorted(summary['category_expense'].items(), key=lambda x: x[1], reverse=True):
        print(f'- {category}: ${value:,.2f}')

if __name__ == '__main__':
    main()
