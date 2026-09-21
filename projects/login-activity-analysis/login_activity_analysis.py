import csv
from io import StringIO

DATA = '''User,Department,SuccessfulLogins,FailedLogins,Country
u001,Finance,42,1,US
u002,Finance,31,8,IN
u003,Engineering,55,2,UK
u004,Sales,26,14,BR
u005,Engineering,47,0,US
u006,Sales,21,19,RU
'''
rows = list(csv.DictReader(StringIO(DATA)))
high_risk = [row['User'] for row in rows if int(row['FailedLogins']) >= 10]
total_attempts = sum(int(row['SuccessfulLogins']) + int(row['FailedLogins']) for row in rows)
failed = sum(int(row['FailedLogins']) for row in rows)
print('=== Login Activity Analysis ===')
print(f'Login attempts: {total_attempts} | Failed attempts: {failed} ({failed / total_attempts * 100:.2f}%)')
print(f'High-risk users: {", ".join(high_risk)}')
print('Recommendation: investigate high-risk users and add stronger controls for unusual login locations.')
