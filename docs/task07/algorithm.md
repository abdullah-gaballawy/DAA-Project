# Algorithm and discussion

## Pseudocode

```text
DESIGN(t):
    choose smallest r in 2..6 with r^t >= 1000
    if none exists: return (false, empty, empty)
    initialize schedule, decoder, path
    DIVIDE(0, 1000, 0)
    return (true, schedule, decoder)

DIVIDE(lo, hi, depth):
    if depth == t:
        decoder[copy(path)] = lo + 1
        return
    capacity = r^(t - depth - 1)
    for digit = 0 .. r-1:
        start = lo + digit * capacity
        if start >= hi: break
        stop = min(hi, start + capacity)
        path[depth] = outcome label for digit
        append abstract assignments to schedule for nonzero digits
        DIVIDE(start, stop, depth + 1)
```

The recursion partitions intervals without overlap and stores exactly one candidate at each nonempty leaf. Two different leaves differ at a depth, which proves the decoder is injective. The algorithm combines independently generated child entries into the common schedule and decoder. It plans all observations in advance, not by waiting for feedback after each recursive level.

Construction: Theta(Nt) time and output space under a unit-cost arithmetic model; O(t) auxiliary space. The tuple-key decoder lookup takes O(t) expected time including hashing.
