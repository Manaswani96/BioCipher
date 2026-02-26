from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .codon_table import CODON_TO_AA, START_CODON, VALID_RNA_BASES


@dataclass(frozen=True)
class TranslationResult:
    protein: List[str]              # e.g., ["Met","Ala","..."]
    started: bool                   # saw start codon?
    stopped: bool                   # ended with STOP?
    stop_codon: Optional[str]       # the stop codon that ended translation
    warnings: List[str]


def split_codons(rna: str, frame: int = 0) -> List[str]:
    rna = rna.strip().upper().replace(" ", "")
    if frame not in (0, 1, 2):
        raise ValueError("frame must be 0, 1, or 2")
    return [rna[i:i+3] for i in range(frame, len(rna), 3)]


def translate_mrna(
    mrna: str,
    *,
    require_start: bool = True,
    stop_at_stop: bool = True,
    frame: int = 0,
) -> TranslationResult:
    """
    Translate mRNA to amino acids.
    - require_start: if True, translation begins only at first AUG (start codon).
    - stop_at_stop: if True, stops at first STOP codon.
    - frame: 0/1/2 reading frame
    """
    mrna = mrna.strip().upper().replace(" ", "")

    for ch in mrna:
        if ch not in VALID_RNA_BASES:
            return TranslationResult(
                protein=[],
                started=False,
                stopped=False,
                stop_codon=None,
                warnings=[f"Invalid character '{ch}' in mRNA. Allowed: A,U,G,C."],
            )

    protein: List[str] = []
    warnings: List[str] = []
    started = not require_start
    stopped = False
    stop_codon: Optional[str] = None

    codons = split_codons(mrna, frame=frame)

    for codon in codons:
        if len(codon) < 3:
            warnings.append(f"Incomplete codon '{codon}' at end of sequence.")
            break

        if require_start and not started:
            if codon == START_CODON:
                started = True
                protein.append("Met")
            continue

        aa = CODON_TO_AA.get(codon, None)
        if aa is None:
            warnings.append(f"Unknown codon '{codon}'.")
            continue

        if aa == "STOP":
            stopped = True
            stop_codon = codon
            if stop_at_stop:
                break
            else:
                continue

        protein.append(aa)

    if require_start and not started:
        warnings.append("Translation did not start (no AUG found in chosen frame).")
    if started and not stopped:
        warnings.append("Translation ended without a STOP codon.")

    return TranslationResult(
        protein=protein,
        started=started,
        stopped=stopped,
        stop_codon=stop_codon,
        warnings=warnings,
    )
