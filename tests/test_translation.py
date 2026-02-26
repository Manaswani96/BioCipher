from biocipher.sequence_engine.translation import translate_mrna

def test_translation_starts_at_aug():
    tr = translate_mrna("CCAUGGCCUAA", require_start=True)
    assert tr.started is True
    assert tr.protein[0] == "Met"

def test_translation_invalid_char():
    tr = translate_mrna("AUGGCCXAA", require_start=True)
    assert tr.protein == []
    assert any("Invalid character" in w for w in tr.warnings)
