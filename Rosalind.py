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
