# EED461 | Design and Analysis of Algorithms - Project 2026/2027

**Ain Shams University - Faculty of Engineering - Computer Engineering and Software Systems**

> **STATUS: STARTER KIT / NOT A FINISHED SOLUTION.** The repository contains API stubs, verifier utilities, test templates, sample inputs, and report/presentation templates. None of the eight solver functions have been implemented yet. A successful infrastructure check does **not** mean the eight algorithms are correct.

## Scope and non-negotiable constraints

- Teams of **up to 8** students; complete **all 8 tasks**.
- Use each task's **mandated algorithmic technique** even if another approach seems easier.
- Any programming language is permitted by the assignment; this starter chooses Python 3.11+.
- Public repository, **meaningful commits by every member**, test inputs.
- PDF report: cover page (names, IDs, individual responsibilities); for every task, assumptions, algorithm explanation, **at least 3 input test cases with output screenshots**, time/space analysis; at the end, clickable GitHub and recorded-presentation links.
- Recorded PowerPoint presentation includes diagrams, figures and examples, **all members speak**, finishes with working demo, **20 minutes maximum**.
- One designated member uploads **only the PDF report** to LMS.

## Task matrix

| # | Task | Mandatory technique | Function |
|---|---|---|---|
| 1 | Coin Removal | Greedy | `removeCoins` |
| 2 | Domino Tiling | Brute Force | `tileDominoes` |
| 3 | Security Switches | Decrease and Conquer | `turnOffSwitches` |
| 4 | Point Coloring | Iterative Improvement | `colorPoints` |
| 5 | King Arthur's Round Table | Dynamic Programming | `seatKnights` |
| 6 | Killing Squares | Dynamic Programming | `breakAllSquares` |
| 7 | Poisoned Wine | Divide and Conquer | `designWineTests` |
| 8 | Colored Tromino Tiling | Divide and Conquer | `tileTromino` |

## Installation (Python 3.11+)

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -e '.[dev]'
python -m pytest -q
```

The current tests verify **imports and independently-written output checkers**. If dependencies cannot be installed yet, `PYTHONPATH=src python -m pytest -q` works in a shell with `pytest` preinstalled (Windows PowerShell: `$env:PYTHONPATH="src"; python -m pytest -q`). Task-specific solver acceptance tests are intentionally skipped until real implementations are written. Do not remove skip markers until the corresponding implementation is complete.

## Recommended team workflow

1. Fill `TEAM.md` with names, student IDs, task owners and reviewers. Remove unused member rows.
2. Agree on the I/O conventions listed in `docs/ASSUMPTIONS_AND_QUESTIONS.md`.
3. Create one issue per task using the task issue template.
4. Work in individual branches, e.g. `feat/task-01-greedy`, submit pull requests and request cross-review.
5. For each task: algorithm, proof/justification, 3+ valid input cases, normal/edge/impossible examples, test outputs and screenshots, complexity.
6. Run `pytest`, review output checker results and export reproducible screenshots.
7. Fill report/presentation templates using REAL results, replace all placeholders, record every teammate speaking, then provide working public links.
8. Run `python scripts/check_submission.py --strict` (release-gate check) and manually verify the links and 20-minute cap.

## Folders

- `src/eed461/tasks/`: separate function stubs; use exact function names from assignment.
- `src/eed461/validators.py`: independent output sanity checkers (not a proof of minimality).
- `tests/`: checker tests + per-task acceptance test placeholders.
- `examples/inputs/`: >=3 sample input records per task (inputs only; not solutions).
- `docs/`: design notes, assumptions, quality checklist and team integration plan.
- `report/`: editable Word template, PDF layout preview, screenshot assets folder.
- `presentation/`: editable PowerPoint deck and diagrams folder.
- `.github/workflows/`: PR checks.

## Submission truthfulness

No completed algorithm, running demo, result screenshot, optimality claim, or complexity bound is provided by this scaffold. All claimed outputs and measured complexities must be verified after implementation. The provided PDF is a **TEMPLATE PREVIEW, NOT A SUBMISSION**.

## Final URLs (fill only after publishing)

- GitHub: `https://github.com/<organization-or-user>/<repo>`
- Recording: `https://<video-host>/<recording>`

This project is based on `docs/EED461_Project_Requirements.pdf` (provided assignment, 3 pages).
