import yaml
from pathlib import Path

def define_env(env):
    @env.macro
    def publications_by_year():
        path = Path(env.variables['extra']['publist_path'])
        full_path = Path(env.project_dir) / "docs" / path
        with open(full_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        grouped = {}
        for pub in data:
            y = pub['year']
            grouped.setdefault(y, []).append(pub)
        return dict(sorted(grouped.items(), reverse=True))