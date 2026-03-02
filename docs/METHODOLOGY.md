# Methodology

## Sequence Engine
Transcription converts DNA to mRNA (T→U) with optional template-strand complement.
Translation maps codons to amino acids using the standard genetic code.
Translation supports frame selection and start/stop codon logic.

## Proteomics Engine
Theoretical spectra are generated from cumulative subpeptide masses including 0.
Experimental matching uses a tolerance-based greedy peak alignment to avoid double counting.
A normalized score is reported as: matched_peaks / total_theoretical_peaks.
