# anki-vocab-coverage

A Python CLI tool for analyzing Anki language learning decks and computing vocabulary coverage across standardized proficiency levels (HSK, JLPT, CEFR) and frequency-based word lists.

---

## Installation

### Install with pipx (recommended)

`pipx` installs Python applications in isolated environments while making their commands available globally.

#### 1. Install pipx

```bash
python -m pip install --user pipx
python -m pipx ensurepath
```

Restart your terminal after installation.

#### 2. Install the package

From GitHub:

```bash
pipx install git+https://github.com/Pisakrus/anki-vocab-coverage.git
```

Or from a local clone:

```bash
git clone https://github.com/Pisakrus/anki-vocab-coverage.git
cd anki-vocab-coverage
pipx install .
```

#### 3. Development installation

If you plan to contribute to the project:

```bash
git clone https://github.com/Pisakrus/anki-vocab-coverage.git
cd anki-vocab-coverage
pipx install --editable .
```