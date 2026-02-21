# 🧬 BioCipher — Code-of-Life Engine

**BioCipher** is a modular computational biology toolkit that treats biological processes as information pipelines.
It simulates the **Central Dogma (DNA → mRNA → Protein)** and connects sequence-level biology with **peptide mass-spectrum inference**.

The project reframes academic bioinformatics exercises into an integrated system where genetic sequences are compiled into proteins and validated through mass-based signals.

---

## ✨ Core Idea

Biology can be viewed as an information system:

```
DNA  →  mRNA  →  Protein  →  Peptide Mass Spectrum  →  Experimental Matching
```

BioCipher implements this flow as a **Genetic Compiler + Proteomic Inference Engine**.

---

## 🧠 Architecture

BioCipher is organized into three main engines:

### 🧬 Sequence Engine — Central Dogma Simulation

Implements deterministic transformations of genetic information.

**Features**

* DNA → mRNA transcription
* mRNA → protein translation
* Codon table lookup (O(1) mapping)
* Frame-aware translation support
* Extensible to ORF detection & reverse translation

---

### ⚖️ Proteomics Engine — Mass-Spectrum Analysis

Bridges protein sequences with experimental mass data.

**Features**

* Theoretical peptide spectrum generation
* Experimental spectrum matching (with tolerance)
* Dipeptide reconstruction from spectral peaks
* Peak overlap scoring

---

### 🔗 BioCipher Pipeline — End-to-End Flow

Connects sequence and proteomics layers into a unified workflow.

Example pipeline:

```
DNA
 ↓ transcription
mRNA
 ↓ translation
Protein
 ↓ theoretical spectrum
Mass peaks
 ↓ matching
Experimental spectrum
```

---

## 📁 Repository Structure

```
biocipher/
  src/biocipher/
    sequence_engine/
      codon_table.py
      transcription.py
      translation.py
      frames.py

    proteomics_engine/
      amino_masses.py
      theoretical_spectrum.py
      spectrum_match.py
      dipeptides.py

    pipeline/
      compile_sequence.py

  notebooks/
    demo_central_dogma.ipynb
    demo_spectrum.ipynb

  challenges/
    transcription_problem.md
    translation_problem.md
    spectrum_problem.md
```

---

## 🚀 Example Use Cases

* Simulate transcription and translation of genetic sequences
* Generate theoretical spectra for candidate peptides
* Compare experimental mass peaks against predicted peptides
* Reconstruct dipeptides from spectral data
* Study how sequence changes affect measurable mass signatures

---

## 🎯 Design Philosophy

BioCipher treats biological sequences as **structured symbolic data** and biological processes as **composable transformations**.

The goal is not only to solve individual bioinformatics problems but to build a reusable framework that connects:

* sequence analysis
* protein inference
* experimental validation

---

## 🔮 Future Work

* Mutation impact analysis (silent / missense / nonsense)
* ORF discovery & ranking
* Codon usage optimization
* Noise-aware spectrum scoring
* Machine learning for peptide-spectrum matching
* Reverse spectrum inference
* Visualization of biological pipelines

---

## 📚 Background

Parts of these implementations were initially developed as computational biology coursework exercises and later refactored into a modular research-style toolkit.

---

## 👩‍💻 Author

Mahi — AI/ML student exploring the intersection of **biological systems, algorithms, and information theory**.

---

## ⭐ Vision

BioCipher explores a simple idea:

> Life is code.
> Genes compile.
> Proteins execute.
> Spectra reveal the runtime.

---
