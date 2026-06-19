# src/anki_vocab_coverage/cli.py
from . import loader
from pathlib import Path

base_hsk_dir = Path(__file__).resolve().parent
json_hsk_path = base_hsk_dir / "datasets" / "hsk2.0" / "hsk2_0.json"

def main():
    print("anki vocab coverage running")
    loader.hello()
    print(loader.get_json_levels(json_hsk_path, 3, 2))