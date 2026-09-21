import csv
from io import StringIO

DATA = '''BugID,Severity,Status,DaysOpen,Team
B001,Critical,Closed,2,Payments
B002,High,Open,9,Checkout
B003,Medium,Closed,4,Mobile
B004,High,Closed,6,Checkout
B005,Critical,Open,14,Payments
B006,Low,Closed,3,Mobile
B007,Medium,Open,11,Search
B008,High,Closed,5,Search
'''
rows = list(csv.DictReader(StringIO(DATA)))
open_bugs = [row for row in rows if row['Status'] == 'Open']
critical_open = sum(row['Severity'] == 'Critical' for row in open_bugs)
average_open_age = sum(int(row['DaysOpen']) for row in open_bugs) / len(open_bugs)
print('=== Software Bug Analysis ===')
print(f'Total bugs: {len(rows)} | Open bugs: {len(open_bugs)} | Critical open bugs: {critical_open}')
print(f'Average age of open bugs: {average_open_age:.1f} days')
print('Recommendation: escalate critical open bugs first and review aging issues with the owning teams.')
