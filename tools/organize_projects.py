import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'script.js'
PROJECTS = ROOT / 'projects'

ALIASES = {
    'sales-performance': 'Sales & Business Analytics',
    'ecommerce-sales': 'E-commerce Analytics',
    'finance-dashboard': 'Finance & Banking',
    'hr-attrition': 'HR & Employee Analytics',
    'marketing-campaigns': 'Marketing Analytics',
}


def slugify(value):
    value = value.lower().replace('&', 'and')
    value = re.sub(r'[^a-z0-9]+', '-', value)
    return value.strip('-')


def catalog_projects():
    source = SOURCE.read_text()
    categories = []
    current = None
    for line in source.splitlines():
        title_match = re.search(r"title:\s*'([^']+)'", line)
        item_match = re.search(r"^\s*'([^']+)',?\s*$", line)
        if title_match:
            current = title_match.group(1)
            categories.append((current, []))
        elif item_match and categories:
            categories[-1][1].append(item_match.group(1))
    mapping = {}
    for category, items in categories:
        for item in items:
            mapping[slugify(item)] = category
    mapping.update({slug: category for slug, category in ALIASES.items()})
    return categories, mapping


def category_folder(index, category):
    return PROJECTS / f'{index:02d}-{slugify(category)}'


def update_references(paths, old, new):
    old_ref = f'projects/{old}/'
    new_ref = f'projects/{new}/'
    for path in paths:
        if path.is_file() and path.suffix.lower() in {'.md', '.py'}:
            text = path.read_text()
            updated = text.replace(old_ref, new_ref)
            if updated != text:
                path.write_text(updated)


def main():
    categories, mapping = catalog_projects()
    category_dirs = {
        category: category_folder(index, category)
        for index, (category, _) in enumerate(categories, start=1)
    }
    for folder in category_dirs.values():
        folder.mkdir(exist_ok=True)

    for category, folder in category_dirs.items():
        readme = folder / 'README.md'
        if not readme.exists():
            readme.write_text(
                f'# {category}\n\n'
                f'This folder contains the data analyst projects in the **{category}** category.\n\n'
                'Each project has its own README and runnable Python starter.\n'
            )

    moved = 0
    for project in list(PROJECTS.iterdir()):
        if not project.is_dir() or project.name.startswith(tuple(f'{i:02d}-' for i in range(1, 100))):
            continue
        category = mapping.get(project.name)
        if not category:
            raise RuntimeError(f'No category mapping for {project.name}')
        destination = category_dirs[category] / project.name
        if destination.exists():
            continue
        shutil.move(str(project), str(destination))
        moved += 1

    all_files = list(ROOT.rglob('*'))
    for project_name, category in mapping.items():
        relative_category = category_dirs[category].relative_to(PROJECTS).as_posix()
        update_references(all_files, project_name, f'{relative_category}/{project_name}')

    print(f'Categories created: {len(category_dirs)}')
    print(f'Projects moved: {moved}')
    print(f'Project folders now: {sum(1 for path in PROJECTS.rglob("*") if path.is_dir() and any(path.glob("README.md")))}')


if __name__ == '__main__':
    main()
