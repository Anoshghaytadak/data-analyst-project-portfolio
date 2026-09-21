import csv
from io import StringIO

DATA = '''Service,Requests,AvgLatencyMs,ErrorRate
Checkout,120000,420,1.8
Search,240000,180,0.7
Payments,95000,510,2.4
Catalog,180000,210,0.9
'''
rows = list(csv.DictReader(StringIO(DATA)))
slowest = max(rows, key=lambda row: float(row['AvgLatencyMs']))
errors = sum(int(row['Requests']) * float(row['ErrorRate']) / 100 for row in rows)
print('=== Application Performance Analytics ===')
print(f'Total requests: {sum(int(row["Requests"]) for row in rows):,}')
print(f'Estimated failed requests: {errors:,.0f}')
print(f'Slowest service: {slowest["Service"]} at {slowest["AvgLatencyMs"]} ms')
print('Recommendation: profile Payments first because it has the highest latency and error rate.')
