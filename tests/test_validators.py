from eed461.models import Toothpick, Tromino
from eed461.validators import (
    validate_coin_sequence, validate_dominoes, validate_switch_toggles,
    validate_point_colors,validate_knight_seating,validate_broken_squares,
    validate_trominoes,
)


def test_coin_fixed_neighbor_sequence():
    assert validate_coin_sequence(['H'],[0])
    assert not validate_coin_sequence(['T'],[0])
    assert not validate_coin_sequence(['H','H'],[0,1])
    assert validate_coin_sequence(['H','T'],[0,1])


def test_domino_checker():
    # n=2, missing opposite colors -> remaining cells coverable by one domino
    assert validate_dominoes(2,(0,0),(0,1),[((1,0),(1,1))])
    assert not validate_dominoes(2,(0,0),(0,1),[((1,0),(0,1))])


def test_switch_checker():
    assert validate_switch_toggles(1,[0])
    assert validate_switch_toggles(2,[0,1])
    assert not validate_switch_toggles(2,[0])


def test_point_balancing_checker():
    points=[(0,0),(1,0),(0,1),(1,1)]
    assert validate_point_colors(points,['B','W','W','B'])
    assert not validate_point_colors(points,['B','B','B','B'])


def test_knight_checker():
    f=[[False,True,True],[True,False,True],[True,True,False]]
    assert validate_knight_seating(f,[0,1,2])
    assert not validate_knight_seating(f,[0,0,1])


def test_toothpick_checker():
    assert validate_broken_squares(1,[Toothpick('H',0,0)])
    assert not validate_broken_squares(1,[])


def test_tromino_checker():
    # Do not fake a 4x4 tiling: check that an empty tiling is correctly rejected.
    assert not validate_trominoes(2,(0,0),[])
