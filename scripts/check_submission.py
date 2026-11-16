"""EED461 release preflight. Run with --strict just before LMS submission.

Checks for unfinished code and evidence. It cannot prove algorithms correct,
check that every student spoke, or guarantee public links work.
"""
from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md', 'TEAM.md', 'docs/ALGORITHM_DESIGNS.md',
    'docs/TEST_MATRIX.md', 'docs/SUBMISSION_CHECKLIST.md',
    'report/EED461_Report_Template.docx',
    'presentation/EED461_Presentation_Template.pptx',
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--strict', action='store_true',
                        help='return error code when the submission is not ready')
    args = parser.parse_args()
    issues = []
    print('EED461 deliverable preflight — no claim of algorithm correctness')
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            issues.append(f'Missing: {rel}')
    task_src = ROOT / 'src/eed461/tasks'
    for idx in range(1, 9):
        matches = list(task_src.glob(f'task_{idx:02d}_*.py'))
        if len(matches) != 1:
            issues.append(f'Task {idx:02d}: expected exactly one solver module')
        elif 'raise NotImplementedError' in matches[0].read_text(encoding='utf-8'):
            issues.append(f'Task {idx:02d}: solver is still NotImplemented')
        test = ROOT / f'tests/test_task_{idx:02d}.py'
        if not test.exists() or 'pytest.mark.skip' in test.read_text(encoding='utf-8'):
            issues.append(f'Task {idx:02d}: acceptance tests are missing or skipped')
        folder = ROOT / f'report/assets/screenshots/task_{idx:02d}'
        present = list(folder.glob('*.png')) if folder.exists() else []
        if len(present) < 3:
            issues.append(f'Task {idx:02d}: only {len(present)} output screenshots (need >=3)')
    team = (ROOT/'TEAM.md').read_text(encoding='utf-8') if (ROOT/'TEAM.md').exists() else ''
    if '[Name]' in team or '[ID]' in team or '[Student ID]' in team:
        issues.append('TEAM.md: group names and/or student IDs are still placeholders')
    # PDF/PowerPoint content requires visual and hyperlink review by a human.
    print(f'{len(issues)} unfinished checks:')
    for issue in issues:
        print(' -', issue)
    print("\nMandatory human verification before submission: actual report content, "
          "three real I/O screenshot pairs per task, correct algorithm and complexity, "
          "all members speak, working recorded demo <=20 minutes, working public "
          "GitHub and recording URLs, and one final PDF LMS upload.")
    return 1 if (args.strict and issues) else 0


if __name__ == '__main__':
    raise SystemExit(main())
