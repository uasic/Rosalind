from tkinter import N


k=27 #DD
m=26 #Dr
n=17 #rr


stevilo_organizmov = k + m + n
seznam_verjetnosti = []

#Prva izbira je DD homozigot
seznam_verjetnosti.append(k/stevilo_organizmov * (k-1)/(stevilo_organizmov-1) )
seznam_verjetnosti.append(k/stevilo_organizmov * m/(stevilo_organizmov-1))
seznam_verjetnosti.append(k/stevilo_organizmov * n/(stevilo_organizmov-1))

#Prva izbira je heterozigot
seznam_verjetnosti.append(m/stevilo_organizmov * k/(stevilo_organizmov-1))
seznam_verjetnosti.append(m/stevilo_organizmov * (m-1)/(stevilo_organizmov-1) * 0.75)
seznam_verjetnosti.append(m/stevilo_organizmov * n/(stevilo_organizmov-1) * 0.5)

#Prv izbira je rr homozigot
seznam_verjetnosti.append(n/stevilo_organizmov * k/(stevilo_organizmov-1))
seznam_verjetnosti.append(n/stevilo_organizmov * m/(stevilo_organizmov-1) * 0.5)

Verjetnost = sum(seznam_verjetnosti)
print(Verjetnost)




