import csv
from io import StringIO

DATA = '''Endpoint,Requests,SuccessRate,AvgResponseMs
/users,450000,99.6,120
/orders,220000,98.9,340
/payments,125000,97.8,510
/reports,45000,99.2,890
'''
rows = list(csv.DictReader(StringIO(DATA)))
most_used = max(rows, key=lambda row: int(row['Requests']))
slowest = max(rows, key=lambda row: float(row['AvgResponseMs']))
weighted_success = sum(int(row['Requests']) * float(row['SuccessRate']) for row in rows) / sum(int(row['Requests']) for row in rows)
print('=== API Usage Analytics ===')
print(f'Total requests: {sum(int(row["Requests"]) for row in rows):,}')
print(f'Weighted success rate: {weighted_success:.2f}%')
print(f'Most used endpoint: {most_used["Endpoint"]} | Slowest: {slowest["Endpoint"]}')
print('Recommendation: optimize Reports response time and investigate Payments reliability.')
