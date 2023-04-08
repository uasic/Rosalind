#path = "C:/Users/urska/Desktop/ROSALIND/rosalind_revc.txt"
#file = open(path, "r")


n = 31
k=4

zaporedje = [1,1]
dolzina_zaporedja = len(zaporedje)
#print(dolzina_zaporedja)

while dolzina_zaporedja <=n:
    nov_par = zaporedje[dolzina_zaporedja-1] + k*zaporedje[dolzina_zaporedja-2]
    #print(nov_par)
    zaporedje.append(nov_par)
    #print(zaporedje)
    dolzina_zaporedja = len(zaporedje)

print(zaporedje[n-1])