"""Normalized output models; confirm ambiguities before submission."""
from dataclasses import dataclass
from typing import Literal

Cell = tuple[int, int]
Domino = tuple[Cell, Cell]

@dataclass(frozen=True)
class Toothpick:
    orientation: Literal['H','V']
    row: int
    col: int

@dataclass(frozen=True)
class Tromino:
    cells: tuple[Cell, Cell, Cell]
    color: str  # use one of {'A', 'B', 'C'}
