# Assumptions that should be agreed before implementation

These are interpretation decisions, **not corrections to the assignment**. Keep the assignment's algorithms and functions authoritative. If the instructor provides clarification, update this file and signatures consistently.

1. **Coin Removal:** `flips` is interpreted as the chronological **removed coin indices** (zero-based), not literal flip events. Each removal flips immediate ORIGINAL neighbor positions that are still present. Gaps never close. Resolve output-name ambiguity with your team.
2. **Domino Tiling:** the PDF says `dominoes: (row,col)[]`, but one domino covers **two** cells. This starter represents each domino as `((r1,c1),(r2,c2))`. Need a final agreement on output format. The two missing cells must be distinct, in-bounds, and opposite chessboard colors.
3. **Security Switches:** all toggle positions are represented by zero-based indices; the rightmost is `n-1`. A valid sequence is not necessarily optimal - a minimality argument is separately required.
4. **Point Coloring:** color outputs are `'B'` and `'W'`; original point order is preserved. All points must be distinct.
5. **King Arthur:** the PDF says each knight is friends with at least half of all `n` knights; clarify interpretation of self-friendship and whether the guarantee uses floor/ceiling. The solver checks only friendships between distinct knights.
6. **Killing Squares:** `(row,col)` alone cannot uniquely identify the toothpick segment since both horizontal and vertical segments occur. This starter uses a `Toothpick(orientation,row,col)` representation. Exact minimality is an explicit requirement, not just breaking each square.
7. **Poisoned Wine:** a death occurs **exactly** 30 days after first poisoned tasting. With a 35-day horizon, recordable death DAYS can encode more than binary live/dead outcomes if testers sample on different days. The problem does not specify when testing starts, day indexing, whether death on feast day is timely, or if multiple tastings per tester are allowed. Document choices; do not assume the eight-tester case is impossible solely because 2^8 < 1000.
8. **Colored Tromino:** input parameter `n` is the exponent, so board side = `2**n`, with n>1. Each L tile covers exactly three of a 2x2 block's four squares. Side-touching trominoes must have different colors; corner-touch is allowed. The coloring constraint makes this more than standard tromino tiling.

## Performance and proof

The assignment supplies no performance target for most tasks and no maximum `n` for several tasks. Choose sensible demonstrable inputs, state bounds, measure if desired, and justify **exact** complexity claims for the algorithm actually submitted. A verifier is not a proof of optimality.
