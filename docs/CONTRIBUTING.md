# Team Git workflow

1. Never commit directly to `main` except agreed setup changes.
2. Make branch `feat/task-XX-short-name` and issue linking the task.
3. Add algorithm + >=3 tests + explanation + complexity + output screenshots.
4. Ask a **different** teammate for review, address comments, merge with traceable author commits.
5. Use conventional commits: `feat(task-01): implement greedy rule`, `test(task-01): add boundary inputs`, `docs(task-01): explain complexity`.
6. Avoid fake screenshots, fabricated runtimes, or a Git history with one person writing all solutions.

## Release gate

- Each task's required algorithmic technique is evident in code and report.
- All real solver tests enabled (no skipped acceptance tests).
- Impossible and boundary cases covered.
- Every screenshot corresponds to a reproducible executed input.
- Report hyperlinks actually open.
- All speakers audible and demo shown in <=20 minutes.
- One final PDF uploaded by one assigned member.
