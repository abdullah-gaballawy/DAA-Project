"""Independent result validators (not proofs of optimality or completeness).

These are helper oracles to catch common mistakes after implementation.
They do not certify that a greedy, DP, or other mandated technique was used.
"""
from collections import defaultdict
from eed461.models import Toothpick, Tromino


def validate_coin_sequence(coins: list[str], removed_indices: list[int]) -> bool:
    """Check legal full clear with fixed ORIGINAL neighborhood."""
    row = [c.upper() for c in coins]
    if any(c not in {'H','T'} for c in row):
        return False
    active = [True] * len(row)
    for idx in removed_indices:
        if not isinstance(idx,int) or not 0 <= idx < len(row) or not active[idx] or row[idx] != 'H':
            return False
        active[idx] = False
        for nb in (idx-1,idx+1):
            if 0 <= nb < len(row) and active[nb]:
                row[nb] = 'T' if row[nb] == 'H' else 'H'
    return not any(active)


def validate_dominoes(n:int, missing1:tuple[int,int], missing2:tuple[int,int], dominoes:list) -> bool:
    if not 2 <= n <= 8 or missing1 == missing2:
        return False
    if any(not (0<=r<n and 0<=c<n) for r,c in (missing1,missing2)):
        return False
    if (sum(missing1)-sum(missing2))%2==0:
        return False
    used=set()
    for domino in dominoes:
        if len(domino)!=2:
            return False
        a,b=domino
        if any(not (0<=r<n and 0<=c<n) for r,c in (a,b)):
            return False
        if abs(a[0]-b[0])+abs(a[1]-b[1])!=1:
            return False
        if a in used or b in used or a in (missing1,missing2) or b in (missing1,missing2):
            return False
        used.update((a,b))
    return used=={(r,c) for r in range(n) for c in range(n)}-{missing1,missing2}


def validate_switch_toggles(n:int, toggles:list[int]) -> bool:
    if n < 1: return False
    on=[True]*n
    for idx in toggles:
        if not isinstance(idx,int) or not 0 <= idx<n:
            return False
        if idx!=n-1 and not (on[idx+1] and not any(on[idx+2:])):
            return False
        on[idx]=not on[idx]
    return not any(on)


def validate_point_colors(points:list[tuple[int,int]], colors:list[str]) -> bool:
    if len(points)!=len(colors) or len(set(points))!=len(points):
        return False
    lines_x,lines_y=defaultdict(list),defaultdict(list)
    for (x,y),color in zip(points,colors):
        if color not in ('B','W'): return False
        lines_x[x].append(color)
        lines_y[y].append(color)
    return all(abs(g.count('B')-g.count('W'))<=1 for g in list(lines_x.values())+list(lines_y.values()))


def validate_knight_seating(friends:list[list[bool]], seating:list[int]) -> bool:
    n=len(friends)
    if n<=2 or any(len(row)!=n for row in friends): return False
    if len(seating)!=n or set(seating)!=set(range(n)): return False
    return all(bool(friends[a][b]) and bool(friends[b][a]) for a,b in zip(seating,seating[1:]+seating[:1]))


def validate_broken_squares(n:int, toothpicks:list[Toothpick]) -> bool:
    if n<1: return False
    removed=set()
    for t in toothpicks:
        if not isinstance(t,Toothpick): return False
        if t.orientation=='H':
            if not (0<=t.row<=n and 0<=t.col<n): return False
        elif t.orientation=='V':
            if not (0<=t.row<n and 0<=t.col<=n): return False
        else: return False
        removed.add(t)
    if len(removed)!=len(toothpicks):return False
    for size in range(1,n+1):
        for row in range(n-size+1):
            for col in range(n-size+1):
                perimeter=[]
                for step in range(size):
                    perimeter.extend((Toothpick('H',row,col+step),Toothpick('H',row+size,col+step),
                                      Toothpick('V',row+step,col),Toothpick('V',row+step,col+size)))
                if all(t not in removed for t in perimeter):return False
    return True


def validate_trominoes(n:int, missing:tuple[int,int], tiles:list[Tromino]) -> bool:
    if n<=1:return False
    side=2**n
    if not all(0<=v<side for v in missing):return False
    allcells=set(); owner={}; colors=set()
    for i,t in enumerate(tiles):
        if not isinstance(t,Tromino) or len(t.cells)!=3 or len(set(t.cells))!=3 or t.color not in {'A','B','C'}:
            return False
        rr=[r for r,c in t.cells]; cc=[c for r,c in t.cells]
        if max(rr)-min(rr)!=1 or max(cc)-min(cc)!=1:return False
        colors.add(t.color)
        for cell in t.cells:
            if not (0<=cell[0]<side and 0<=cell[1]<side) or cell in owner or cell==missing:return False
            owner[cell]=i; allcells.add(cell)
    if allcells != {(r,c) for r in range(side) for c in range(side)}-{missing}:return False
    for (r,c),i in owner.items():
        for nb in ((r+1,c),(r,c+1)):
            j=owner.get(nb)
            if j is not None and j!=i and tiles[i].color==tiles[j].color:
                return False
    return True
