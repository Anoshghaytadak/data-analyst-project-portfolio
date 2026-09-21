import csv
from io import StringIO

DATA = '''Page,Sessions,BounceRate,ConversionRate,LoadSeconds
Home,12000,42,3.2,2.1
Pricing,6800,28,7.4,1.8
Blog,9400,61,1.5,3.6
Checkout,5200,19,9.1,2.7
'''
rows = list(csv.DictReader(StringIO(DATA)))
slowest = max(rows, key=lambda row: float(row['LoadSeconds']))
best_conversion = max(rows, key=lambda row: float(row['ConversionRate']))
print('=== Website Performance Dashboard ===')
print(f'Sessions: {sum(int(row["Sessions"]) for row in rows):,}')
print(f'Slowest page: {slowest["Page"]} at {slowest["LoadSeconds"]} seconds')
print(f'Best converting page: {best_conversion["Page"]} at {best_conversion["ConversionRate"]}%')
print('Recommendation: improve Blog loading speed and preserve the strong Checkout conversion experience.')
