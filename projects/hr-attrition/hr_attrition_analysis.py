import csv
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / 'data' / 'employee_attrition.csv'


def load_rows():
    with open(DATA_FILE, newline='') as file:
        return list(csv.DictReader(file))


def summarize(rows):
    department_totals = defaultdict(int)
    department_attrition = defaultdict(int)
    overtime_totals = defaultdict(int)
    overtime_attrition = defaultdict(int)

    for row in rows:
        department = row['Department']
        overtime = row['Overtime']
        department_totals[department] += 1
        overtime_totals[overtime] += 1
        if row['Attrition'] == 'Yes':
            department_attrition[department] += 1
            overtime_attrition[overtime] += 1

    return {
        'employees': len(rows),
        'attrition': sum(1 for row in rows if row['Attrition'] == 'Yes'),
        'department_totals': dict(department_totals),
        'department_attrition': dict(department_attrition),
        'overtime_totals': dict(overtime_totals),
        'overtime_attrition': dict(overtime_attrition),
    }


def rate(number, total):
    return number / total * 100 if total else 0


def main():
    summary = summarize(load_rows())
    print('=== HR Attrition Analysis ===')
    print(f'Total Employees: {summary["employees"]}')
    print(f'Employees Who Left: {summary["attrition"]}')
    print(f'Overall Attrition Rate: {rate(summary["attrition"], summary["employees"]):.2f}%')

    print('\nAttrition by Department:')
    for department in sorted(summary['department_totals']):
        print(f'- {department}: {rate(summary["department_attrition"].get(department, 0), summary["department_totals"][department]):.2f}%')

    print('\nAttrition by Overtime:')
    for overtime in sorted(summary['overtime_totals']):
        print(f'- {overtime}: {rate(summary["overtime_attrition"].get(overtime, 0), summary["overtime_totals"][overtime]):.2f}%')


if __name__ == '__main__':
    main()
