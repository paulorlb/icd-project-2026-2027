"""Reading rules shared by the project's notebooks."""

from pathlib import Path

import pandas as pd


def read_table(path: Path) -> pd.DataFrame:
    """Read an unchanged, comma-separated source table with string identifiers."""
    return pd.read_csv(path, dtype=str, keep_default_na=False, na_values=[""])
