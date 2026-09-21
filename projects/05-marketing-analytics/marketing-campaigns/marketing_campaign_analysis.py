import csv
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / 'data' / 'campaign_performance.csv'


def load_rows():
    with open(DATA_FILE, newline='') as file:
        return list(csv.DictReader(file))


def summarize(rows):
    channel_metrics = defaultdict(lambda: {'impressions': 0, 'clicks': 0, 'conversions': 0, 'spend': 0.0, 'revenue': 0.0})
    for row in rows:
        metrics = channel_metrics[row['Channel']]
        for field in ('impressions', 'clicks', 'conversions'):
            metrics[field] += int(row[field.capitalize()])
        metrics['spend'] += float(row['Spend'])
        metrics['revenue'] += float(row['Revenue'])
    return dict(channel_metrics)


def main():
    metrics = summarize(load_rows())
    print('=== Marketing Campaign Analysis ===')
    for channel, values in sorted(metrics.items()):
        ctr = values['clicks'] / values['impressions'] * 100
        conversion_rate = values['conversions'] / values['clicks'] * 100
        roi = (values['revenue'] - values['spend']) / values['spend'] * 100
        print(f'\n{channel}')
        print(f'- CTR: {ctr:.2f}%')
        print(f'- Conversion Rate: {conversion_rate:.2f}%')
        print(f'- ROI: {roi:.2f}%')
        print(f'- Revenue: ${values["revenue"]:,.2f}')


if __name__ == '__main__':
    main()
