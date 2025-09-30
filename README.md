# 🧬 DNA Sequence Analyzer  

A simple Python-based tool for analyzing DNA sequences from FASTA files.  
This project demonstrates basic **bioinformatics techniques** such as sequence parsing, GC content calculation, motif searching, and nucleotide frequency visualization.  

---

## 🔹 Features
- Reads DNA sequences from `.fasta` files  
- Calculates sequence length and GC content  
- Finds motifs (e.g., `"ATG"` start codons)  
- Counts nucleotide frequencies (`A`, `T`, `G`, `C`)  
- Creates a bar chart visualization of nucleotide frequencies  

---

## 🔹 Example Output
```text
Sequence ID: Test_Sequence
Sequence Length: 60
First 50 bases: ATGCGTATCGATCGATCGTAGCTAGCTAGCGATATCGATCGTAGCTAG
GC Content: 51.67%
Motif 'ATG' found at positions: [0, 43]
Base Frequencies: {'A': 15, 'T': 15, 'G': 15, 'C': 15}
