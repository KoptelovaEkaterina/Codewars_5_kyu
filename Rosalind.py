# Counting letters 'A', 'C', 'G', 'T' in string of file rosalind_dna.txt

with open("rosalind_dna.txt") as file:
    nucleotides = file.read()
    print(nucleotides.count('A'), nucleotides.count('C'), nucleotides.count('G'), nucleotides.count('T') )

# Making RNA from DNA, replacing T by U

with open("rosalind_rna.txt") as file:
    nucleotides = file.read()
    print(nucleotides.replace('T', 'U'))
    
# Reverse complement of DNA strand using Python
    
from Bio.Seq import Seq

seq = Seq(nucleotides)

print(seq.reverse_complement())
  

