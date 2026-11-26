import sys
from pathlib import Path
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from eed461.tasks.task_07_poisoned_wine import designWineTests, simulate

@pytest.mark.parametrize('testers,radix', [(10,2),(8,3),(4,6)])
def test_every_barrel(testers, radix):
    possible, schedule, decoder = designWineTests(testers)
    assert possible and len(schedule) == testers and len(decoder) == 1000
    assert len(schedule[0]) == radix - 1
    for barrel in range(1,1001):
        signature = simulate(schedule, barrel)
        assert decoder[signature] == barrel
        assert all(x is None or 30 <= x <= 34 for x in signature)

@pytest.mark.parametrize('testers', [0,1,2,3])
def test_impossible(testers):
    assert designWineTests(testers) == (False, [], {})

@pytest.mark.parametrize('testers', [-1, 1.5, True])
def test_invalid(testers):
    with pytest.raises(ValueError):
        designWineTests(testers)

def test_no_signal():
    _, schedule, decoder = designWineTests(8)
    assert simulate(schedule, 1) == (None,) * 8
    assert decoder[(None,) * 8] == 1
