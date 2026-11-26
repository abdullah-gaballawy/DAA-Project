# Task 07 — Poisoned Wine

Academic simulation only. The implementation uses recursive radix partitioning and represents the puzzle as timed outcome signals.

From repository root (Windows PowerShell or Bash):

```sh
python src/eed461/tasks/task07.py --testers 10 --barrel 731
python src/eed461/tasks/task07.py --testers 8 --barrel 1000
python src/eed461/tasks/task07.py --testers 3 --barrel 731
python src/eed461/tasks/task07.py --testers 4 --barrel 1
python -m pip install pytest
python -m pytest -q tests/test_task07_poisoned_wine.py
```

Open `docs/task07/demo.html` in a browser for an offline interactive demonstration. `examples/inputs/task07.json` contains repeatable inputs. CLI output and screenshot evidence are in this directory. Python is the canonical solver; the HTML is a separate equivalent demonstration.

## API
`designWineTests(testers)` returns `(possible, schedule, decoder)`. `schedule[t][day]` lists one-based candidate IDs; `decoder` maps tuples of observed signal days (`None` means no signal) to one-based IDs. Impossible inputs return `(False, [], {})`; invalid inputs raise `ValueError`. The deadline is handled conservatively by ending signals by day 34. Both required cases are feasible; three testers are impossible even if day 35 is included.

## Integration
The filenames assume the earlier EED461 scaffold. Inspect the current team repository first, adapt imports and filenames to the established conventions if necessary, and never overwrite a teammate's files or shared templates. No GitHub changes were made by this package.
