from biocipher.pipeline.compile_flow import peptide_vs_experiment

experimental = [101.05, 138.08, 187.10, 238.13, 312.18]
peptides = ["GAS", "GAT", "KGV", "LAK"]

for pep in peptides:
    res = peptide_vs_experiment(pep, experimental, tolerance=0.05)
    print(f"\nPeptide: {res.peptide}")
    print("Theoretical:", res.theoretical)
    print("Matched pairs:", res.matched_pairs)
    print("Matches:", res.match_count, "Score:", round(res.score, 3))
