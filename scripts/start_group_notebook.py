"""Create a group-owned notebook from a teacher-maintained lesson notebook."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
LESSON_NOTEBOOKS = {
    "W06S01": PROJECT_ROOT / "notebooks" / "lessons" / "W06S01_practice.ipynb",
}


def group_slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")
    if not slug:
        raise argparse.ArgumentTypeError("group name must contain a letter or number")
    return slug


def cell_text(cell: dict) -> str:
    source = cell.get("source", [])
    return source if isinstance(source, str) else "".join(source)


def replace_source(cell: dict, text: str) -> None:
    original = cell.get("source", [])
    cell["source"] = text if isinstance(original, str) else text.splitlines(keepends=True)


def adapt_source(text: str) -> str:
    replacements = (
        ('"outputs" / "lessons" / "w06"', '"outputs" / "project" / "w06"'),
        ("outputs/lessons/w06", "outputs/project/w06"),
        (
            "attachment:DataScienceForSocialSciences.png",
            "../lessons/_assets/shared/DataScienceForSocialSciences.png",
        ),
        ("./_assets/", "../lessons/_assets/"),
        ("(_assets/", "(../lessons/_assets/"),
        ('src="_assets/', 'src="../lessons/_assets/'),
    )
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("lesson_id", choices=sorted(LESSON_NOTEBOOKS))
    parser.add_argument("group", type=group_slug, help="short group name used in the filename")
    parser.add_argument("--destination", type=Path, help="optional output path, mainly for testing")
    args = parser.parse_args()

    source_path = LESSON_NOTEBOOKS[args.lesson_id]
    destination = args.destination or (
        PROJECT_ROOT / "notebooks" / "project" / f"{args.lesson_id}_{args.group}.ipynb"
    )
    if not destination.is_absolute():
        destination = PROJECT_ROOT / destination
    destination = destination.resolve()

    if destination.exists():
        raise FileExistsError(f"Refusing to overwrite existing notebook: {destination}")

    notebook = json.loads(source_path.read_text(encoding="utf-8"))
    for cell in notebook.get("cells", []):
        replace_source(cell, adapt_source(cell_text(cell)))
        if cell.get("cell_type") == "code":
            cell["execution_count"] = None
            cell["outputs"] = []

    metadata = notebook.setdefault("metadata", {})
    metadata.setdefault("kernelspec", {})["display_name"] = "Python 3 (icd-project)"
    course_metadata = metadata.setdefault("mtad", {})
    course_metadata["version"] = "group"
    course_metadata["derived_from"] = source_path.relative_to(PROJECT_ROOT).as_posix()

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )
    print(destination.relative_to(PROJECT_ROOT).as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
