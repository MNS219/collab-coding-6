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
├── CONTRIBUTING.md
├── main.py
├── README.md
├── test_add_module.py
├── test_k.py
└── test_p.py
```