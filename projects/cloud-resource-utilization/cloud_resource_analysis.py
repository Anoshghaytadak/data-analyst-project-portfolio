import csv
from io import StringIO

DATA = '''Resource,Type,CPUPercent,MemoryPercent,HoursUnused
vm-prod-01,VM,72,68,4
vm-prod-02,VM,18,25,38
vm-dev-01,VM,9,14,96
db-prod-01,Database,64,74,2
'''
rows = list(csv.DictReader(StringIO(DATA)))
underused = [row['Resource'] for row in rows if float(row['CPUPercent']) < 20]
average_cpu = sum(float(row['CPUPercent']) for row in rows) / len(rows)
print('=== Cloud Resource Utilization ===')
print(f'Average CPU utilization: {average_cpu:.1f}%')
print(f'Underutilized resources: {", ".join(underused)}')
print(f'Unused hours identified: {sum(float(row["HoursUnused"]) for row in rows):.0f}')
print('Recommendation: schedule or right-size underutilized development resources to reduce waste.')
