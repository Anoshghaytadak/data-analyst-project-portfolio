import csv
from io import StringIO

DATA = '''Plan,Customers,MonthlyPrice,Churned,NewCustomers
Basic,420,29,18,42
Pro,280,79,9,31
Enterprise,54,399,1,6
'''
rows = list(csv.DictReader(StringIO(DATA)))
monthly_recurring_revenue = sum(int(row['Customers']) * float(row['MonthlyPrice']) for row in rows)
churn_rate = sum(int(row['Churned']) for row in rows) / sum(int(row['Customers']) for row in rows) * 100
print('=== SaaS Subscription Analytics ===')
print(f'MRR: ${monthly_recurring_revenue:,.2f} | Customers: {sum(int(row["Customers"]) for row in rows)}')
print(f'Customer churn rate: {churn_rate:.2f}%')
print(f'New customers: {sum(int(row["NewCustomers"]) for row in rows)}')
print('Recommendation: protect Enterprise accounts while testing retention offers for the larger Basic segment.')
