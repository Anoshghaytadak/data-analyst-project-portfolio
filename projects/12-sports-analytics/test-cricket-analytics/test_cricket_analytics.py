"""Starter analysis for Test Cricket Analytics."""

from statistics import mean

PROJECT = 'Test Cricket Analytics'
CATEGORY = 'Sports Analytics'
SAMPLE_VALUES = [72, 81, 67, 89, 76]


def main():
    average = mean(SAMPLE_VALUES)
    highest = max(SAMPLE_VALUES)
    lowest = min(SAMPLE_VALUES)
    print(f"=== {PROJECT} ===")
    print(f"Category: {CATEGORY}")
    print(f"Sample KPI average: {average:.1f}")
    print(f"Sample KPI range: {lowest} to {highest}")
    print("Next step: replace SAMPLE_VALUES with a cleaned dataset and document the business recommendation.")


if __name__ == '__main__':
    main()
