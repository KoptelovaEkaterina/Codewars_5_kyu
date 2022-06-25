# Count letters 'A', 'C', 'G', 'T' in string of file rosalind_dna.txt

with open("rosalind_dna.txt") as file:
    nucleotides = file.read()
    print(nucleotides.count('A'), nucleotides.count('C'), nucleotides.count('G'), nucleotides.count('T') )
