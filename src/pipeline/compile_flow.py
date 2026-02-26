from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from biocipher.sequence_engine.encoding import encode_amino_acids_to_mrna
from biocipher.sequence_engine.translation import translate_mrna
from biocipher.proteomics_engine.theoretical_spectrum import theoretical_spectrum
from biocipher.proteomics_engine.spectrum_match import MatchResult, match_spectra, score_match


@dataclass(frozen=True)
class CompileFlowResult:
    mrna: str
    protein: List[str]
    spectrum: Optional[List[float]]
    notes: List[str]


def compile_amino_acids_to_protein_and_spectrum(amino_acids: List[str]) -> CompileFlowResult:
    """
    'Compiler' mode: AA names -> mRNA (representative codons) -> translate -> (optional) spectrum.
    Note: Using representative codons may not preserve original biology; this is an educational pipeline.
    """
    notes: List[str] = []
    mrna = encode_amino_acids_to_mrna(amino_acids)
    tr = translate_mrna(mrna, require_start=False, stop_at_stop=True, frame=0)

    notes.extend(tr.warnings)
    protein = tr.protein

    # If protein can be represented in 1-letter codes, spectrum can be computed on peptide strings.
    # Here we only build spectrum if we can map 3-letter -> 1-letter later; keeping it simple for now.
    return CompileFlowResult(mrna=mrna, protein=protein, spectrum=None, notes=notes)


def peptide_vs_experiment(peptide: str, experimental: List[float], tolerance: float = 0.05) -> MatchResult:
    theo = theoretical_spectrum(peptide)
    pairs = match_spectra(theo, experimental, tolerance=tolerance)
    return MatchResult(
        peptide=peptide,
        theoretical=theo,
        matched_pairs=pairs,
        match_count=len(pairs),
        score=score_match(theo, pairs),
    )
