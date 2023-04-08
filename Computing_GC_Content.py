from msilib import sequence


data_set = open("C:\\Users\\urska\\Desktop\\rosalind_gc.txt","r")
#print(data_set.read())

sequence_length=0
ID_dict = {}

for l in data_set:
    line = l.strip()
    if line[0]==">":
        if sequence_length>0:
            ratio=(G_number+C_number)/(sequence_length)
            ID_dict[ID]=ratio
        ID = line[1:]
        sequence_length=0
        G_number = 0
        C_number = 0
        #print(ID)
    else: 
        print(len(line))
        sequence_length=sequence_length+len(line)
        print(sequence_length)
        for i in line:
            if i == "C":
                C_number = C_number + 1
                #print(C_number)
            if i == "G":
                G_number = G_number + 1
                #print(G_number)


ratio=(G_number+C_number)/sequence_length
ID_dict[ID]=ratio

print(ID_dict)

max_ratio=max(ID_dict.values())
max_ID=max(ID_dict, key=ID_dict.get)
print(max_ID)
print(max_ratio*100)