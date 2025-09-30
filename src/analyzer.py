from Bio import SeqIO
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the sequence
record = SeqIO.read("sequence.fasta", "fasta")
sequence = str(record.seq)

print(f"Sequence ID: {record.id}")
print(f"Sequence Length: {len(sequence)}")
print(f"First 50 bases: {sequence[:50]}")

# 2. Calculate GC Content
gc_count = sequence.count("G") + sequence.count("C")
gc_content = (gc_count / len(sequence)) * 100
print(f"GC Content: {gc_content:.2f}%")

# 3. Motif search (example: "ATG" start codon)
motif = "ATG"
positions = [i for i in range(len(sequence)) if sequence.startswith(motif, i)]
print(f"Motif '{motif}' found at positions: {positions}")

# 4. Base frequency count
freq = {base: sequence.count(base) for base in "ATGC"}
print("Base Frequencies:", freq)

# 5. Visualization
sns.barplot(x=list(freq.keys()), y=list(freq.values()))
plt.title("Nucleotide Frequency")
plt.xlabel("Base")
plt.ylabel("Count")
plt.savefig("nucleotide_freq.png")  # saves as image
plt.show()
