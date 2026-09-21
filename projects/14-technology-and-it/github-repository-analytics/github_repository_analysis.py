import csv
from io import StringIO

DATA = '''Repository,Stars,Forks,OpenIssues,Contributors,Commits30Days
analytics-dashboard,128,34,7,12,46
etl-pipeline,84,19,3,8,31
forecasting-model,212,51,14,18,72
internal-tools,36,8,2,5,12
'''
rows = list(csv.DictReader(StringIO(DATA)))
most_popular = max(rows, key=lambda row: int(row['Stars']))
active = max(rows, key=lambda row: int(row['Commits30Days']))
print('=== GitHub Repository Analytics ===')
print(f'Total stars: {sum(int(row["Stars"]) for row in rows)} | Total contributors: {sum(int(row["Contributors"]) for row in rows)}')
print(f'Most popular: {most_popular["Repository"]} with {most_popular["Stars"]} stars')
print(f'Most active: {active["Repository"]} with {active["Commits30Days"]} commits in 30 days')
print('Recommendation: combine popularity and recent activity when deciding which repositories need maintenance.')
