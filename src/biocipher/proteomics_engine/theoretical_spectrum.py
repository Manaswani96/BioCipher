from __future__ import annotations

from typing import List

from .amino_masses import AMINO_ACID_MASSES


def theoretical_spectrum(peptide: str, *, decimals: int = 2) -> List[float]:
    """
    Build a simple theoretical spectrum consisting of cumulative subpeptide masses
    (including 0), rounded to `decimals`.
    """
    peptide = peptide.strip().upper()
    if not peptide:
        return [0.0]

    for aa in peptide:
        if aa not in AMINO_ACID_MASSES:
            raise ValueError(f"Unknown amino acid '{aa}' in peptide '{peptide}'.")

    spectrum: List[float] = [0.0]
    n = len(peptide)

    for i in range(n):
        mass = 0.0
        for j in range(i, n):
            mass += AMINO_ACID_MASSES[peptide[j]]
            spectrum.append(round(mass, decimals))

    return sorted(spectrum)
