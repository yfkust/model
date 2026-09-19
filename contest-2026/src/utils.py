from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "figures"
TABLE_DIR = ROOT / "tables"
OUTPUT_DIR = ROOT / "output"

for d in [DATA_DIR, FIG_DIR, TABLE_DIR, OUTPUT_DIR]:
    d.mkdir(exist_ok=True)
