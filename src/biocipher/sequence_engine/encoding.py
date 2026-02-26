from __future__ import annotations

from typing import Dict, Iterable, List

# Minimal single-codon encoder (your lab used one codon per AA).
AA_NAME_TO_CODON: Dict[str, str] = {
    "ala": "GCU", "arg": "CGU", "asn": "AAU", "asp": "GAU",
    "cys": "UGU", "gln": "CAA", "glu": "GAA", "gly": "GGU",
    "his": "CAU", "ile": "AUU", "leu": "CUU", "lys": "AAA",
    "met": "AUG", "phe": "UUU", "pro": "CCU", "ser": "UCU",
    "thr": "ACU", "trp": "UGG", "tyr": "UAU", "val": "GUU",
    "stop": "UAA",
}

def encode_amino_acids_to_mrna(amino_acids: Iterable[str]) -> str:
    """
    Encode an amino acid name sequence to mRNA using a single representative codon per AA.
    Example input: ["val","gly","trp",...]
    Unknown names raise ValueError (research vibe = strict).
    """
    codons: List[str] = []
    for aa in amino_acids:
        key = aa.strip().lower()
        if key not in AA_NAME_TO_CODON:
            raise ValueError(f"Unknown amino acid name: '{aa}'")
        codons.append(AA_NAME_TO_CODON[key])
    return "".join(codons)
