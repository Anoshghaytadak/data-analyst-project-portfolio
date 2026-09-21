import csv
from io import StringIO

DATA = '''Channel,Conversations,FirstResponseMinutes,CSAT,Escalations
Email,4200,180,3.8,210
Chat,6800,4,4.4,160
Phone,1900,6,4.1,95
SelfService,5100,1,4.6,42
'''
rows = list(csv.DictReader(StringIO(DATA)))
best_csat = max(rows, key=lambda row: float(row['CSAT']))
print('=== Customer Support Analytics ===')
print(f'Conversations: {sum(int(row["Conversations"]) for row in rows):,}')
print(f'Best CSAT channel: {best_csat["Channel"]} ({best_csat["CSAT"]}/5)')
print(f'Total escalations: {sum(int(row["Escalations"]) for row in rows)}')
print('Recommendation: expand self-service content and reduce dependence on slow Email support.')
