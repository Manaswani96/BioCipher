from biocipher.proteomics_engine.theoretical_spectrum import theoretical_spectrum

def test_theoretical_spectrum_contains_zero():
    spec = theoretical_spectrum("GAS")
    assert spec[0] == 0.0
    assert len(spec) > 1
