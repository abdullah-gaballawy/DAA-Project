import importlib

MODULES = [
    'task_01_coin_removal', 'task_02_domino_tiling', 'task_03_security_switches',
    'task_04_point_coloring', 'task_05_knights', 'task_06_killing_squares',
    'task_07_poisoned_wine', 'task_08_colored_tromino',
]

def test_each_task_module_exists():
    for name in MODULES:
        assert importlib.import_module('eed461.tasks.'+name)
