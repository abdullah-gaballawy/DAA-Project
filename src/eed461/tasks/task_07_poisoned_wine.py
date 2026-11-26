"""EED461 Task 7: abstract timed-outcome puzzle (simulation only)."""
from __future__ import annotations
import argparse

N = 1000
LATENCY = 30
MAX_RADIX = 6  # Use days 0..4; all signals arrive by day 34.


def designWineTests(testers: int):
    """Return (possible, schedule, decoder).

    schedule[t][day] is a list of 1-based barrel IDs; t is zero-based.
    decoder maps tuples of outcome days (None = no signal) to barrel IDs.
    An impossible instance returns (False, [], {}). No real testing is intended.
    """
    if isinstance(testers, bool) or not isinstance(testers, int) or testers < 0:
        raise ValueError('testers must be a nonnegative integer')
    radix = next((r for r in range(2, MAX_RADIX + 1) if r ** testers >= N), None)
    if radix is None:
        return False, [], {}
    schedule = [{d: [] for d in range(radix - 1)} for _ in range(testers)]
    decoder = {}
    path = [None] * testers

    def divide(lo: int, hi: int, depth: int):
        if depth == testers:
            assert hi - lo == 1
            decoder[tuple(path)] = lo + 1
            return
        capacity = radix ** (testers - depth - 1)
        for digit in range(radix):
            start = lo + digit * capacity
            if start >= hi:
                break
            stop = min(hi, start + capacity)
            path[depth] = None if digit == 0 else LATENCY + digit - 1
            if digit:
                schedule[depth][digit - 1].extend(range(start + 1, stop + 1))
            divide(start, stop, depth + 1)

    divide(0, N, 0)
    return True, schedule, decoder


def simulate(schedule, barrel: int):
    """Derive a synthetic outcome directly from the generated schedule."""
    if not 1 <= barrel <= N:
        raise ValueError('barrel must be in 1..1000')
    result = []
    for days in schedule:
        matches = [day + LATENCY for day, ids in days.items() if barrel in ids]
        assert len(matches) <= 1
        result.append(matches[0] if matches else None)
    return tuple(result)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--testers', type=int, required=True)
    parser.add_argument('--barrel', type=int, default=731)
    args = parser.parse_args()
    if not 1 <= args.barrel <= N:
        parser.error('--barrel must be in 1..1000')
    try:
        possible, schedule, decoder = designWineTests(args.testers)
    except ValueError as e:
        parser.error(str(e))
    print(f'Testers: {args.testers} | Candidate barrels: {N}')
    print('Possible:', 'YES' if possible else 'NO')
    if not possible:
        print(f'Maximum outcomes under full 35-day window: {7 ** args.testers}')
        print('No guaranteed unique identification.')
        return
    radix = len(schedule[0]) + 1
    print(f'Radix: {radix} | Capacity: {radix ** args.testers}')
    print(f'Simulated hidden barrel: {args.barrel}')
    signature = simulate(schedule, args.barrel)
    print('Outcome days:', ', '.join('-' if x is None else str(x) for x in signature))
    print('Decoded barrel:', decoder[signature])
    print('Result:', 'PASS' if decoder[signature] == args.barrel else 'FAIL')
    print(f'Latest planned signal day: {LATENCY + radix - 2}')


if __name__ == '__main__':
    main()
