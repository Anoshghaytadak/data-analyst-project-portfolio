import csv
from io import StringIO
from datetime import date

DATA = '''AssetID,Type,Status,PurchaseYear,AnnualCost,Owner
A001,Laptop,Active,2023,240,Finance
A002,Laptop,Repair,2020,180,Sales
A003,Server,Active,2021,2400,Platform
A004,Monitor,Active,2019,80,HR
A005,Laptop,Retired,2018,120,Marketing
A006,Network,Active,2022,900,Platform
'''
rows = list(csv.DictReader(StringIO(DATA)))
current_year = date.today().year
old_assets = [row['AssetID'] for row in rows if current_year - int(row['PurchaseYear']) >= 5]
print('=== IT Asset Management ===')
print(f'Assets: {len(rows)} | Active: {sum(row["Status"] == "Active" for row in rows)} | Annual cost: ${sum(float(row["AnnualCost"]) for row in rows):,.2f}')
print(f'Repair or retired assets: {sum(row["Status"] in ("Repair", "Retired") for row in rows)}')
print(f'Assets at least five years old: {", ".join(old_assets)}')
print('Recommendation: replace aging laptops and track repair costs by department.')
