import csv
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / 'data' / 'ecommerce_sales.csv'


def load_rows():
    with open(DATA_FILE, newline='') as file:
        return list(csv.DictReader(file))


def summarize(rows):
    total_revenue = 0.0
    category_sales = defaultdict(float)
    payment_usage = defaultdict(int)
    weekday_sales = defaultdict(float)

    for row in rows:
        revenue = float(row['Revenue'])
        category = row['Category']
        payment = row['PaymentMethod']
        weekday = row['Weekday']

        total_revenue += revenue
        category_sales[category] += revenue
        payment_usage[payment] += 1
        weekday_sales[weekday] += revenue

    return {
        'total_revenue': total_revenue,
        'category_sales': dict(category_sales),
        'payment_usage': dict(payment_usage),
        'weekday_sales': dict(weekday_sales),
    }


def main():
    rows = load_rows()
    summary = summarize(rows)

    print('=== E-commerce Sales Analysis ===')
    print(f'Total Revenue: ${summary["total_revenue"]:,.2f}')
    print('Top Category by Revenue:')
    for category, value in sorted(summary['category_sales'].items(), key=lambda x: x[1], reverse=True):
        print(f'- {category}: ${value:,.2f}')

    print('\nPayment Method Usage:')
    for method, count in sorted(summary['payment_usage'].items(), key=lambda x: x[1], reverse=True):
        print(f'- {method}: {count}')

if __name__ == '__main__':
    main()
