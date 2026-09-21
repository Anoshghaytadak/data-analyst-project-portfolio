import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'script.js'
PROJECTS = ROOT / 'projects'


def slugify(value):
    value = value.lower().replace('&', 'and')
    value = re.sub(r"[^a-z0-9]+", '-', value)
    return value.strip('-')


def parse_catalog():
    source = SOURCE.read_text()
    categories = []
    current_category = None
    for line in source.splitlines():
        title_match = re.search(r"title:\s*'([^']+)'", line)
        item_match = re.search(r"^\s*'([^']+)',?\s*$", line)
        if title_match:
            current_category = title_match.group(1)
            categories.append((current_category, []))
        elif item_match and categories:
            categories[-1][1].append(item_match.group(1))
    return categories


def write_project(category, topic):
    folder = PROJECTS / slugify(topic)
    if folder.exists():
        return False
    folder.mkdir(parents=True)
    script_name = f'{slugify(topic).replace("-", "_")}.py'
    readme = f'''# {topic}\n\n## Category\n{category}\n\n## Business question\nHow can an analyst use data to measure performance, identify patterns, and recommend an improvement for **{topic}**?\n\n## Suggested analysis\n- Define the business KPI and the decision it supports\n- Clean missing values, duplicates, and inconsistent categories\n- Compare performance over time, across segments, and against a target\n- Explain the most important insight and its business impact\n\n## Starter project\n\nRun the included Python starter from the repository root:\n\n```bash\npython3 projects/{folder.name}/{script_name}\n```\n\nThe starter produces a reproducible analysis brief. Replace its sample rows with a real dataset from a trusted public source and add charts in Excel, Power BI, Tableau, SQL, or Python.\n\n## Portfolio deliverables\n- Cleaned dataset\n- SQL queries or Python notebook\n- KPI dashboard\n- Three evidence-based insights\n- One practical recommendation\n'''
    script = f'''"""Starter analysis for {topic}."""\n\nfrom statistics import mean\n\nPROJECT = {topic!r}\nCATEGORY = {category!r}\nSAMPLE_VALUES = [72, 81, 67, 89, 76]\n\n\ndef main():\n    average = mean(SAMPLE_VALUES)\n    highest = max(SAMPLE_VALUES)\n    lowest = min(SAMPLE_VALUES)\n    print(f"=== {{PROJECT}} ===")\n    print(f"Category: {{CATEGORY}}")\n    print(f"Sample KPI average: {{average:.1f}}")\n    print(f"Sample KPI range: {{lowest}} to {{highest}}")\n    print("Next step: replace SAMPLE_VALUES with a cleaned dataset and document the business recommendation.")\n\n\nif __name__ == '__main__':\n    main()\n'''
    (folder / 'README.md').write_text(readme)
    (folder / script_name).write_text(script)
    return True


def main():
    created = 0
    topics = 0
    for category, items in parse_catalog():
        for topic in items:
            topics += 1
            created += write_project(category, topic)
    print(f'Catalog topics found: {topics}')
    print(f'New project starters created: {created}')


if __name__ == '__main__':
    main()
