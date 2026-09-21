import csv
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / 'data' / 'sample_sales.csv'


def load_rows():
    with open(DATA_FILE, newline='') as file:
        return list(csv.DictReader(file))


def summarize(rows):
    total_revenue = 0.0
    total_profit = 0.0
    total_units = 0
    region_revenue = defaultdict(float)
    product_revenue = defaultdict(float)
    month_revenue = defaultdict(float)

    for row in rows:
        revenue = float(row['Revenue'])
        profit = float(row['Profit'])
        units = int(row['Units'])
        region = row['Region']
        product = row['Product']
        month = row['Month']

        total_revenue += revenue
        total_profit += profit
        total_units += units

        region_revenue[region] += revenue
        product_revenue[product] += revenue
        month_revenue[month] += revenue

    return {
        'total_revenue': total_revenue,
        'total_profit': total_profit,
        'total_units': total_units,
        'region_revenue': dict(region_revenue),
        'product_revenue': dict(product_revenue),
        'month_revenue': dict(month_revenue),
    }


def top_item(mapping):
    return max(mapping.items(), key=lambda x: x[1])[0]


def main():
    rows = load_rows()
    summary = summarize(rows)

    best_region = top_item(summary['region_revenue'])
    best_product = top_item(summary['product_revenue'])
    best_month = top_item(summary['month_revenue'])
    avg_order_value = summary['total_revenue'] / len(rows)
    profit_margin = (summary['total_profit'] / summary['total_revenue']) * 100 if summary['total_revenue'] else 0

    print('=== Sales Performance Dashboard ===')
    print(f'Total Revenue: ${summary["total_revenue"]:,.2f}')
    print(f'Total Profit: ${summary["total_profit"]:,.2f}')
    print(f'Total Units Sold: {summary["total_units"]}')
    print(f'Average Order Value: ${avg_order_value:,.2f}')
    print(f'Profit Margin: {profit_margin:.2f}%')
    print(f'Best Region: {best_region}')
    print(f'Best Product: {best_product}')
    print(f'Best Month: {best_month}')

    print('\nRegion Revenue:')
    for region, value in sorted(summary['region_revenue'].items()):
        print(f'- {region}: ${value:,.2f}')

if __name__ == '__main__':
    main()
