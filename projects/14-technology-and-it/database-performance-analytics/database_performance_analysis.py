import csv
from io import StringIO

DATA = '''QueryType,Executions,AvgDurationMs,FailureRate
Read,850000,42,0.2
Write,210000,115,0.8
Report,42000,980,2.1
Maintenance,18000,640,0.4
'''
rows = list(csv.DictReader(StringIO(DATA)))
slowest = max(rows, key=lambda row: float(row['AvgDurationMs']))
weighted_duration = sum(int(row['Executions']) * float(row['AvgDurationMs']) for row in rows) / sum(int(row['Executions']) for row in rows)
print('=== Database Performance Analytics ===')
print(f'Executions: {sum(int(row["Executions"]) for row in rows):,}')
print(f'Weighted average duration: {weighted_duration:.1f} ms')
print(f'Slowest query type: {slowest["QueryType"]} at {slowest["AvgDurationMs"]} ms')
print('Recommendation: optimize Report queries with indexing, caching, or pre-aggregated tables.')
