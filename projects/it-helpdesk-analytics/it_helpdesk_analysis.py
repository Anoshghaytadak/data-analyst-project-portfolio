import csv
from io import StringIO

DATA = '''TicketID,Category,Priority,ResolutionHours,Satisfaction
H001,Hardware,High,7,4
H002,Software,Medium,18,4
H003,Network,High,11,3
H004,Access,Low,5,5
H005,Hardware,Medium,22,3
H006,Network,High,15,2
H007,Software,Low,8,5
H008,Access,Medium,9,4
'''

rows = list(csv.DictReader(StringIO(DATA)))
average_resolution = sum(float(row['ResolutionHours']) for row in rows) / len(rows)
average_satisfaction = sum(float(row['Satisfaction']) for row in rows) / len(rows)
category_counts = {category: sum(row['Category'] == category for row in rows) for category in sorted({row['Category'] for row in rows})}
print('=== IT Helpdesk Analytics ===')
print(f'Tickets: {len(rows)} | Average resolution: {average_resolution:.1f} hours | Satisfaction: {average_satisfaction:.2f}/5')
print(f'Tickets by category: {category_counts}')
print('Recommendation: prioritize Network tickets because they combine high priority with longer resolution times.')
