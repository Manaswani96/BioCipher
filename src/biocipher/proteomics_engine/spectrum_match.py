from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass(frozen=True)
class MatchResult:
    peptide: str
    theoretical: List[float]
    matched_pairs: List[Tuple[float, float]]  # (theo, exp)
    match_count: int
    score: float  # simple normalized score


def match_spectra(
    theoretical: List[float],
    experimental: List[float],
    *,
    tolerance: float = 0.05,
) -> List[Tuple[float, float]]:
    """
    One-to-one greedy matching: each theoretical peak can match at most one experimental peak.
    This avoids double-counting and feels more 'researchy' than nested loops.
    """
    theo = sorted(theoretical)
    exp = sorted(experimental)
    matched: List[Tuple[float, float]] = []

    i = j = 0
    while i < len(theo) and j < len(exp):
        t = theo[i]
        e = exp[j]
        diff = t - e

        if abs(diff) <= tolerance:
            matched.append((t, e))
            i += 1
            j += 1
        elif diff < 0:
            i += 1
        else:
            j += 1

    return matched


def score_match(theoretical: List[float], matched_pairs: List[Tuple[float, float]]) -> float:
    if not theoretical:
        return 0.0
    return len(matched_pairs) / len(theoretical)
