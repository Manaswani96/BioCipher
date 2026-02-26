from __future__ import annotations

def dna_to_mrna(dna: str, *, assume_coding_strand: bool = True) -> str:
    """
    Transcribe DNA to mRNA.
    - If assume_coding_strand=True: just replace T -> U.
    - If False: treat input as template strand and create complementary RNA.
      (A<->U, T->A, C<->G, G<->C) with T in DNA.
    """
    dna = dna.strip().upper().replace(" ", "")

    if assume_coding_strand:
        return dna.replace("T", "U")

    # template strand -> complementary RNA
    comp = {"A": "U", "T": "A", "C": "G", "G": "C"}
    out = []
    for ch in dna:
        if ch not in comp:
            raise ValueError(f"Invalid DNA base '{ch}'. Allowed: A,T,C,G.")
        out.append(comp[ch])
    return "".join(out)
