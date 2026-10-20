"""Run dependency-free structural checks for the course project repository."""

from __future__ import annotations

import base64
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
LESSON_NOTEBOOK = ROOT / "notebooks" / "lessons" / "W06S01_practice.ipynb"
EXPECTED_DATA = {
    "authorship_2020_2026.csv": "41a9e5fbc512d3d7e015e4d0dc7beed6daa3d2d15049e94bab90d582d3604d73",
    "publications_2020_2026.csv": "60b1ab3f6ce49d7edcb65506f5adffb9c3f279f3ea1065e4240b3744a87961be",
    "publications_authors_2020_2026.csv": "ca6b83deaaee435ea329e882897c9bdbc157f5cf05d512c5d9ef48da2c363b8d",
}
REQUIRED_PATHS = (
    "README.md",
    "environment.yml",
    "pyproject.toml",
    ".gitignore",
    "data/raw/README.md",
    "data/processed/.gitkeep",
    "outputs/.gitkeep",
    "notebooks/lessons/W06S01_practice.ipynb",
    "notebooks/project/README.md",
    "src/icd_project_aux/__init__.py",
    "docs/research_plan_v0.md",
    "docs/evidence_register.md",
    "docs/contributions.csv",
    "docs/ai_use_log.csv",
    "reports/README.md",
    "scripts/start_group_notebook.py",
    "scripts/verify_repository.py",
)
LEGACY_PATHS = (
    "assets",
    "notebooks/W06S01_practice.ipynb",
    "outputs/w06",
)


class Results:
    def __init__(self) -> None:
        self.failures = 0
        self.warnings = 0

    def pass_(self, message: str) -> None:
        print(f"PASS  {message}")

    def fail(self, message: str) -> None:
        self.failures += 1
        print(f"FAIL  {message}")

    def warn(self, message: str) -> None:
        self.warnings += 1
        print(f"WARN  {message}")


def source_text(cell: dict) -> str:
    source = cell.get("source", [])
    return source if isinstance(source, str) else "".join(source)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def git(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args],
        check=False,
        capture_output=True,
        text=True,
    )


def check_notebook_images(notebook: dict, results: Results) -> None:
    markdown_pattern = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
    html_pattern = re.compile(r"<img[^>]+src=[\"']([^\"']+)[\"']", re.IGNORECASE)
    checked = 0

    for cell in notebook.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        text = source_text(cell)
        references = markdown_pattern.findall(text) + html_pattern.findall(text)
        for raw_reference in references:
            reference = raw_reference.strip().strip("<>").split(maxsplit=1)[0]
            if reference.startswith(("http://", "https://", "data:", "#")):
                continue
            checked += 1
            if reference.startswith("attachment:"):
                name = reference.removeprefix("attachment:")
                attachments = cell.get("attachments", {})
                payloads = attachments.get(name, {})
                if not payloads:
                    results.fail(f"missing notebook attachment: {name}")
                    continue
                try:
                    for payload in payloads.values():
                        base64.b64decode(payload, validate=True)
                except (ValueError, TypeError):
                    results.fail(f"invalid base64 notebook attachment: {name}")
                else:
                    results.pass_(f"notebook attachment decodes: {name}")
                continue

            image_path = (LESSON_NOTEBOOK.parent / unquote(reference)).resolve()
            try:
                image_path.relative_to(ROOT)
            except ValueError:
                results.fail(f"notebook image escapes the repository: {reference}")
            else:
                if image_path.is_file():
                    results.pass_(f"notebook image resolves: {reference}")
                else:
                    results.fail(f"missing notebook image: {reference}")

    if checked == 0:
        results.fail("no local notebook images or attachments were found")


def main() -> int:
    results = Results()

    for relative in REQUIRED_PATHS:
        if (ROOT / relative).exists():
            results.pass_(f"required path exists: {relative}")
        else:
            results.fail(f"required path is missing: {relative}")

    for relative in LEGACY_PATHS:
        if (ROOT / relative).exists():
            results.fail(f"legacy path still exists: {relative}")
        else:
            results.pass_(f"legacy path is absent: {relative}")

    environment_text = (ROOT / "environment.yml").read_text(encoding="utf-8")
    environment_match = re.search(r"(?m)^name:\s*([^\s#]+)", environment_text)
    if environment_match and environment_match.group(1) == "icd-project":
        results.pass_("environment.yml declares icd-project")
    else:
        results.fail("environment.yml must declare name: icd-project")

    try:
        notebook = json.loads(LESSON_NOTEBOOK.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        results.fail(f"lesson notebook is not valid JSON: {error}")
        notebook = {}
    else:
        results.pass_(f"lesson notebook is valid nbformat {notebook.get('nbformat')}")
        check_notebook_images(notebook, results)
        all_source = "\n".join(source_text(cell) for cell in notebook.get("cells", []))
        expected_output_code = 'PROJECT_ROOT / "outputs" / "lessons" / "w06"'
        if expected_output_code in all_source:
            results.pass_("lesson notebook writes under outputs/lessons/w06")
        else:
            results.fail("lesson notebook output directory is not outputs/lessons/w06")
        kernel = notebook.get("metadata", {}).get("kernelspec", {}).get("display_name", "")
        if "icd-project" in kernel:
            results.pass_(f"notebook kernel matches the project environment: {kernel}")
        else:
            results.warn(f"select the icd-project kernel before Run All; notebook currently says {kernel!r}")

    for filename, expected_hash in EXPECTED_DATA.items():
        path = ROOT / "data" / "raw" / filename
        if not path.exists():
            results.warn(f"raw input is absent from this clone: {filename}")
        elif sha256(path) == expected_hash:
            results.pass_(f"raw input hash matches: {filename}")
        else:
            results.fail(f"raw input hash differs: {filename}")

    output_root = ROOT / "outputs"
    misplaced_outputs = []
    for path in output_root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT).as_posix()
        if relative == "outputs/.gitkeep":
            continue
        if not relative.startswith(("outputs/lessons/", "outputs/project/")):
            misplaced_outputs.append(relative)
    if misplaced_outputs:
        for relative in misplaced_outputs:
            results.fail(f"generated output is outside an owned output tree: {relative}")
    else:
        results.pass_("generated outputs use outputs/lessons or outputs/project")

    tracked_outputs = git("ls-files", "--", "outputs")
    if tracked_outputs.returncode != 0:
        results.warn("Git was unavailable while checking tracked outputs")
    else:
        tracked = [line for line in tracked_outputs.stdout.splitlines() if line]
        unexpected = [path for path in tracked if path != "outputs/.gitkeep"]
        if unexpected:
            for path in unexpected:
                results.fail(f"generated output is tracked by Git: {path}")
        else:
            results.pass_("Git tracks no generated outputs")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    required_headings = (
        "## Purpose and ownership",
        "## Structure",
        "## Set up the environment",
        "## Data",
        "## Run order",
        "## Generated and reference outputs",
        "## Project records",
        "## Git synchronization",
        "## Verification gates",
        "## Clean-clone test",
    )
    missing_headings = [heading for heading in required_headings if heading not in readme]
    if missing_headings:
        for heading in missing_headings:
            results.fail(f"README section is missing: {heading}")
    else:
        results.pass_("README contains the complete project contract")

    remotes = git("remote")
    if remotes.returncode == 0:
        names = set(remotes.stdout.split())
        if "origin" not in names:
            results.warn("Git remote 'origin' is not configured")
        if "upstream" not in names:
            results.warn("Git remote 'upstream' is not configured")

    status = git("status", "--porcelain")
    if status.returncode == 0 and status.stdout.strip():
        results.warn("working tree contains uncommitted changes")
    elif status.returncode == 0:
        results.pass_("working tree is clean")

    print(f"\nSummary: {results.failures} failure(s), {results.warnings} warning(s)")
    return 1 if results.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
