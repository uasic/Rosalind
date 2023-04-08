

path = "C:/Users/urska/Desktop/ROSALIND/rosalind_revc.txt"

file = open(path, "r")
DNA = file.read()

dictionary = {'T': 'A', 'A':'T', 'G': 'C', 'C': 'G', 'x': None, 'y': None, 'z': None}
transTable = DNA.maketrans(dictionary)
complement = DNA.translate(transTable)
#print(complement)

reverse_complement = complement[::-1]
print(reverse_complement)