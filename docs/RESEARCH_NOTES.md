# BioCipher Research Notes 
## Scope
BioCipher models biological information flow as a pipeline:
DNA → mRNA → Protein → Mass Spectrum → Matching

## Implemented Modules
- Sequence Engine: transcription, translation
- Proteomics Engine: theoretical spectrum, tolerant matching

## Design Choices
- Single source of truth for codon table + mass table
- Deterministic functions + testable outputs
- Tolerance-based matching to reflect experimental noise

## Experiments Log
### Exp-001: Translation sanity check
Input: AUGGCCAUGGUGCCCCAGAACUGAGUUG
Output: [Met, Ala, ...]
Notes: start/stop handling verified.

### Exp-002: Spectrum matching baseline
Experimental peaks: [101.05, 138.08, 187.10, 238.13, 312.18]
Peptides tested: GAS, GAT, KGV, LAK
Metric: match_count, normalized score
