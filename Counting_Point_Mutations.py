from msilib import sequence


file = open("C:\\Users\\urska\\Desktop\\rosalind_hamm.txt","r")
#print(file.read())

#every line in its own list
sequence = file.readlines()
data = [x.strip() for x in sequence]
#print(data)

number_of_seq = len(data)
#print(number_of_seq)


nucleotide=0
sequence1=0
sequence2=1
hamming = 0

while nucleotide in range(0,len(data[0])):
    #print(data)
    #print(len(data[0]))
    #print(data[sequence1][nucleotide])
    #print(data[sequence2][nucleotide])
    if data[sequence1][nucleotide] != data[sequence2][nucleotide]:
        hamming = hamming + 1
    nucleotide = nucleotide + 1

print(hamming)



