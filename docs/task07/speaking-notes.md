# The King's Dilemma — recording notes (~2 minutes, excluding demo)

**Act I (20 seconds):** One of one thousand barrels is anomalous. The feast is in 35 days and the observation delay is exactly 30 days. Can ten, or even eight, testers identify the unknown candidate? This is an abstract mathematical simulation.

**Act II (30 seconds):** Binary outcomes provide 1,024 signatures for ten testers, but only 256 for eight. Distinguishing two timed outcomes and absence creates a ternary alphabet. Eight testers now have 6,561 signatures. The dot fields show coverage of the required 1,000 candidates. Both required cases are feasible.

**Act III (35 seconds):** Choose the smallest radix with enough capacity. Divide the interval into disjoint subranges, assign a distinct outcome label to each child, and recurse until each leaf contains one candidate. Each leaf is stored in a unique decoder. Different leaves diverge at a depth; the plan is constructed before observation begins.

**Act IV (25 seconds):** Eleven automated tests passed, including 3,000 exhaustive checks across ten, eight and four testers. Three testers are impossible even with seven outcomes each. Construction time and explicit output space are Theta(Nt); auxiliary recursion space is O(t).

**Demo:** Open docs/task07/demo.html. Show ten testers with candidate 731, eight with candidate 1000, and three with any candidate. If needed, show the Python CLI and pytest.

The PowerPoint includes manual click-to-advance fade transitions and per-slide speaker notes. Background art, dot fields, and captured stdout are images; text and the recursion diagram are editable.
