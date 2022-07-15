def DNA_strand(dna):
    comp_dna = {"A":"T","T":"A","G":"C","C":"G"}
    return ''.join([comp_dna[x] for x in dna])

print(DNA_strand("AAAA")) # Should return TTTT
print(DNA_strand("ATTGC")) # Should return TAACG
