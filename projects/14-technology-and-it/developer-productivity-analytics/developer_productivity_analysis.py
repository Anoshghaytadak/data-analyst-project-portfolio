import csv
from io import StringIO

DATA = '''Team,Developers,CompletedTickets,CodeReviews,AverageCycleHours
Platform,6,84,112,31
Payments,5,71,95,38
Mobile,4,52,68,44
Data,4,63,89,27
'''
rows = list(csv.DictReader(StringIO(DATA)))
most_productive = max(rows, key=lambda row: int(row['CompletedTickets']))
fastest = min(rows, key=lambda row: float(row['AverageCycleHours']))
print('=== Developer Productivity Analytics ===')
print(f'Completed tickets: {sum(int(row["CompletedTickets"]) for row in rows)}')
print(f'Most tickets completed: {most_productive["Team"]} ({most_productive["CompletedTickets"]})')
print(f'Fastest cycle time: {fastest["Team"]} ({fastest["AverageCycleHours"]} hours)')
print('Recommendation: study Data team practices while addressing Mobile cycle-time bottlenecks.')
