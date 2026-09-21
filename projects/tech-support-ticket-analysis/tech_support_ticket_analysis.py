import csv
from io import StringIO

DATA = '''TicketID,Channel,IssueType,FirstResponseMinutes,ResolutionHours,Reopened
T001,Email,Login,18,4,No
T002,Chat,Payment,3,2,No
T003,Email,Integration,44,19,Yes
T004,Phone,Login,7,3,No
T005,Chat,Integration,5,11,Yes
T006,Email,Payment,31,8,No
'''
rows = list(csv.DictReader(StringIO(DATA)))
average_response = sum(float(row['FirstResponseMinutes']) for row in rows) / len(rows)
reopened = sum(row['Reopened'] == 'Yes' for row in rows)
print('=== Tech Support Ticket Analysis ===')
print(f'Tickets: {len(rows)} | Average first response: {average_response:.1f} minutes | Reopened: {reopened}')
print(f'Average resolution: {sum(float(row["ResolutionHours"]) for row in rows) / len(rows):.1f} hours')
print('Recommendation: improve Integration knowledge articles because those tickets take longer and are reopened more often.')
