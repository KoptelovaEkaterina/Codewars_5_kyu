# Translating RNA into Protein

with open("rosalind_prot.txt") as file:
    seq = file.readline().rstrip("\n")     

    
table = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L", "UCU":"S", 
        "UCC":"S", "UCA":"S", "UCG":"S", "UAU":"Y", "UAC":"Y", "UAA":"", "UAG":"", 
        "UGU":"C", "UGC":"C", "UGA":"", "UGG":"W", "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L", "CCU":"P", 
        "CCC":"P", "CCA":"P", "CCG":"P", "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q", "CGU":"R", "CGC":"R", "CGA":"R", 
        "CGG":"R", "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M", "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T", "AAU":"N", 
        "AAC":"N", "AAA":"K", "AAG":"K", "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R", "GUU":"V", "GUC":"V", "GUA":"V", 
        "GUG":"V", "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A", "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E", "GGU":"G", 
        "GGC":"G", "GGA":"G", "GGG":"G",}  


def translate_rna_to_protein(seq):
    protein =""
    for nuc in range(0, len(seq), 3):
        codon = seq[nuc:nuc + 3]
        protein += table[codon]  
    print(protein)


print(translate_rna_to_protein(seq))


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
 
    
# Select the sequence with the highest GC composition
# answer from:
# https://www.youtube.com/watch?v=mw4FSbDro0A
# https://www.youtube.com/watch?v=7k9nCLrHipQ

def readFile(filePath):
    with open(filePath, 'r') as file:
        return [l.strip() for l in file.readlines()] 

def gc_content(seq):
    return round(
        ((seq.count('C') + seq.count('G')) / len(seq) * 100), 6) 

FASTAFile = readFile("rosalind_gc.txt")
FASTADict = {}
FASTALabel = ""

for line in FASTAFile:
    if '>' in line:
        FASTALabel = line 
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line
# print(FASTADict)

RESULTDict = {key: gc_content(value) for (key, value) in FASTADict.items()}
MaxGCKey = max(RESULTDict, key=RESULTDict.get)

print(f'{MaxGCKey[1:]}\n{RESULTDict[MaxGCKey]}')
