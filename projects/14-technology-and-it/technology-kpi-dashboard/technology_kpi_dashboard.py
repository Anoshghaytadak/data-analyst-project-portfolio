import csv
from io import StringIO

DATA = '''Metric,Actual,Target
System Uptime,99.85,99.90
Ticket SLA,91.2,95.0
Deployment Success,98.1,97.0
Security Resolution Hours,18,12
Customer CSAT,4.3,4.5
'''
rows = list(csv.DictReader(StringIO(DATA)))
print('=== Technology KPI Dashboard ===')
for row in rows:
    actual = float(row['Actual'])
    target = float(row['Target'])
    status = 'On target' if (actual >= target if row['Metric'] != 'Security Resolution Hours' else actual <= target) else 'Needs attention'
    print(f'{row["Metric"]}: {row["Actual"]} vs {row["Target"]} - {status}')
print('Recommendation: focus improvement on SLA, security resolution time, and customer satisfaction.')
