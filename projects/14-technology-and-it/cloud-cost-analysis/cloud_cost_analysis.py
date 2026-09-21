import csv
from io import StringIO

DATA = '''Service,Environment,MonthlyCost,Owner
Compute,Production,4200,Platform
Database,Production,3100,Data
Storage,Production,1250,Platform
Compute,Development,1800,Engineering
Database,Development,900,Data
Storage,Development,700,Engineering
'''
rows = list(csv.DictReader(StringIO(DATA)))
by_service = {}
for row in rows:
    by_service[row['Service']] = by_service.get(row['Service'], 0) + float(row['MonthlyCost'])
most_expensive = max(by_service, key=by_service.get)
print('=== Cloud Cost Analysis ===')
print(f'Total monthly cost: ${sum(float(row["MonthlyCost"]) for row in rows):,.2f}')
print(f'Largest cost area: {most_expensive} at ${by_service[most_expensive]:,.2f}')
print(f'Production share: {sum(float(row["MonthlyCost"]) for row in rows if row["Environment"] == "Production") / sum(float(row["MonthlyCost"]) for row in rows) * 100:.1f}%')
print('Recommendation: review Compute utilization and enforce environment-level budgets.')
