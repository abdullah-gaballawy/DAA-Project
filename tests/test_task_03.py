"""Task 03 solver acceptance tests."""
from eed461.tasks.task_03_security_switches import turnOffSwitches


def is_valid_solution(n, toggles):
    """Replay the toggles on a row of n switches and check every move is legal
    and that all switches end up OFF. Switches are numbered 1..n from the left."""
    state = [True] * (n + 1)  # index 0 unused; True = ON

    for i in toggles:
        if i < 1 or i > n:
            return False
        if i < n:
            # right neighbor must be ON
            if not state[i + 1]:
                return False
            # all switches farther right must be OFF
            for j in range(i + 2, n + 1):
                if state[j]:
                    return False
        state[i] = not state[i]

    for j in range(1, n + 1):
        if state[j]:
            return False
    return True


def test_task_03_normal_case():
    # n = 3: known answer from the Chinese Rings puzzle
    min_moves, toggles = turnOffSwitches(3)
    assert min_moves == 5
    assert toggles == [3, 1, 3, 2, 3]
    assert is_valid_solution(3, toggles)


def test_task_03_boundary_case():
    # n = 1: only the rightmost switch, one move
    min_moves, toggles = turnOffSwitches(1)
    assert min_moves == 1
    assert toggles == [1]
    assert is_valid_solution(1, toggles)


def test_task_03_third_case():
    # n = 4: 10 moves, and every move must be legal
    min_moves, toggles = turnOffSwitches(4)
    assert min_moves == 10
    assert len(toggles) == min_moves
    assert is_valid_solution(4, toggles)