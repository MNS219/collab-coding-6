# Collaborative Coding — 6


A small team project simulating a real-world GitHub workflow. Each contributor adds **one themed function** (Utility Toolkit), with docs and tests. The Admin integrates them via `driver.py`.


## Project Goals
- Practice Git branching, PRs, code reviews, and conflict resolution.
- Write clear, documented, and tested functions.
- Integrate via a single driver and ensure CI passes.


## Tech Stack
- Language: Python 3.10+
- Tests: pytest
- CI: GitHub Actions (runs pytest)


## Repo Structure
collab-coding-6
```bash
.
├── driver.py
├── modules
│   └── init.py
├── README.md
└── tests

```
## Getting Started
```bash
# Clone
git clone https://github.com/<org-or-user>/collab-coding-<groupID>.git
cd collab-coding-<groupID>


# Setup
python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate
pip install -r requirements.txt


# Run tests
pytest -q


# Run driver
python driver.py