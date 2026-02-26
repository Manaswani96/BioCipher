from biocipher.sequence_engine.encoding import encode_amino_acids_to_mrna
from biocipher.sequence_engine.translation import translate_mrna

amino_acid_sequence = ["val","gly","trp","ser","ala","val","ser","trp","val","leu"]
mrna = encode_amino_acids_to_mrna(amino_acid_sequence)
print("mRNA:", mrna)

tr = translate_mrna("AUGGCCAUGGUGCCCCAGAACUGAGUUG", require_start=True)
print("Protein:", tr.protein)
print("Warnings:", tr.warnings)
