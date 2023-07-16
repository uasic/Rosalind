RNA_codon_table = open("C:\\Users\\urska\\Desktop\\RNA_codon_table.txt", "r")
RNA_codon_dic = {}
for line in RNA_codon_table:
    line.strip("\n")
    key, value = line.split(",")
    RNA_codon_dic[key] = value.rstrip("\n")
    #print(line)

#print(RNA_codon_dic)

RNA_string = open("C:\\Users\\urska\\Desktop\\RNA_string.txt", "r")
mRNA = RNA_string.read()
#print(mRNA)

nuc_1 = 0
codons = []
while nuc_1<= len(mRNA)-3:
    codons.append(mRNA[nuc_1:(nuc_1+3)])
    #print(codons)
    nuc_1 = nuc_1 + 3
#print(codons)

protein = []
for codon in codons:
    #print(codon)
    amino_acid = RNA_codon_dic.get(codon)
    if amino_acid == "Stop":
        break
    #print(amino_acid)
    protein.append(amino_acid.strip())
#print(protein)
protein_seq = "".join(protein)
print(protein_seq)

    
