import csv
from io import StringIO

DATA = '''Sprint,PlannedPoints,CompletedPoints,Defects,Deployments
Sprint 1,42,36,8,3
Sprint 2,45,44,5,4
Sprint 3,48,39,11,2
Sprint 4,50,47,6,5
'''
rows = list(csv.DictReader(StringIO(DATA)))
completion = sum(int(row['CompletedPoints']) for row in rows) / sum(int(row['PlannedPoints']) for row in rows) * 100
defect_rate = sum(int(row['Defects']) for row in rows) / sum(int(row['CompletedPoints']) for row in rows)
print('=== Software Development Analytics ===')
print(f'Planned points: {sum(int(row["PlannedPoints"]) for row in rows)} | Completed: {sum(int(row["CompletedPoints"]) for row in rows)} ({completion:.1f}%)')
print(f'Defects per completed point: {defect_rate:.3f}')
print(f'Deployments: {sum(int(row["Deployments"]) for row in rows)}')
print('Recommendation: review Sprint 3 planning because delivery fell while defects increased.')
