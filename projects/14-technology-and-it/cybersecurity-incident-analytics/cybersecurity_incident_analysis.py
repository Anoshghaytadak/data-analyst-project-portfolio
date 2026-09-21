import csv
from io import StringIO

DATA = '''IncidentID,Type,Severity,ResponseMinutes,Resolved
C001,Phishing,High,35,Yes
C002,Malware,Critical,18,Yes
C003,Unauthorized Access,High,52,No
C004,Phishing,Medium,44,Yes
C005,DDoS,Critical,27,Yes
C006,Unauthorized Access,High,61,No
'''
rows = list(csv.DictReader(StringIO(DATA)))
critical = sum(row['Severity'] == 'Critical' for row in rows)
unresolved = sum(row['Resolved'] == 'No' for row in rows)
average_response = sum(float(row['ResponseMinutes']) for row in rows) / len(rows)
print('=== Cybersecurity Incident Analytics ===')
print(f'Incidents: {len(rows)} | Critical: {critical} | Unresolved: {unresolved}')
print(f'Average response time: {average_response:.1f} minutes')
print('Recommendation: reduce response time for unauthorized access incidents and close the unresolved queue.')
