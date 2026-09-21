import csv
from io import StringIO

DATA = '''UserSegment,Users,WeeklyActiveUsers,FeatureAUsers,FeatureBUsers
New,620,248,186,93
Returning,840,571,512,428
Power,210,202,199,196
'''
rows = list(csv.DictReader(StringIO(DATA)))
for row in rows:
    row['EngagementRate'] = int(row['WeeklyActiveUsers']) / int(row['Users']) * 100
best = max(rows, key=lambda row: row['EngagementRate'])
print('=== Software User Engagement ===')
print(f'Users: {sum(int(row["Users"]) for row in rows):,} | Weekly active users: {sum(int(row["WeeklyActiveUsers"]) for row in rows):,}')
print(f'Strongest segment: {best["UserSegment"]} at {best["EngagementRate"]:.1f}% weekly engagement')
print('Feature A adoption: {:.1f}%'.format(sum(int(row['FeatureAUsers']) for row in rows) / sum(int(row['Users']) for row in rows) * 100))
print('Recommendation: improve onboarding for New users and use Power users to identify successful product behaviors.')
