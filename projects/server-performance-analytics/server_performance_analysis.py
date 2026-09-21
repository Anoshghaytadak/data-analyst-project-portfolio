import csv
from io import StringIO

DATA = '''Server,CPUPercent,MemoryPercent,DiskPercent,UptimePercent
app-01,68,72,61,99.98
app-02,81,84,75,99.91
app-03,34,41,58,99.99
db-01,76,89,82,99.80
'''
rows = list(csv.DictReader(StringIO(DATA)))
high_memory = max(rows, key=lambda row: float(row['MemoryPercent']))
lowest_uptime = min(rows, key=lambda row: float(row['UptimePercent']))
print('=== Server Performance Analytics ===')
print(f'Average CPU: {sum(float(row["CPUPercent"]) for row in rows) / len(rows):.1f}%')
print(f'Highest memory usage: {high_memory["Server"]} at {high_memory["MemoryPercent"]}%')
print(f'Lowest uptime: {lowest_uptime["Server"]} at {lowest_uptime["UptimePercent"]}%')
print('Recommendation: investigate database memory pressure and uptime incidents on db-01.')
