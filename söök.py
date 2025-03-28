
# kirjuta programm mis
# küsib kasutajalt tsükli sees
# kas tal on hapukapsas
# - kui kasutajal ei ole, siis öeldakse et saab hautist
# kas tal on pott
# - kui kasutajal potti ei ole, siis öeldakse et suppi teha ei saa
# kas tal on vett
# - kui kasutajal vett ei ole, siis öeldakse et saab mulgikapsaid teha
# kas tal on kartulit
# kas tal on puljongit
# kas kasutajal on midagi muud kapis (ei/kasutajavastus)
# - kui kasutajal ei ole, siis öeldakse midagi eelnevatest sobivatest vastustest
# - kui kasutajal on, siis öeldakse et saab ühepajatoitu
# kogu arvutamine peab toimuma loogiliste tehetega and or not



                
kapsas = False
kasonkapsas = ""
pott=False
vett=False
kartul=False
puljon=False
kapis=False
Miskapis=""

while(kapsas == False and kasonkapsas == ""):
    kasonkapsas = input("kas sul on kapsst")
    if kasonkapsas == "jah":
        kapsas = True
    else:
        print("saad hautist")
            
while(pott == False):
    kasonpott = input("kas sul on pott")
    if kasonpott == "jah":
        pott = True
    else:
        print("supp ei saa")
            
while(vett == False):
    kasonvett = input("kas sul on vett")
    if kasonvett == "jah":
        vett = True
    else:
        print("saab mulgikapsaid teha")

while(kartul == False):
    kasonkartul = input("kas sul on kartulit")
    if kasonkartul == "jah":
        kartul = True
    if kasonkartul== "ei":
        kartul = eikartul
        
        

print("on puljongit")
puljong=input()

while(kapis == False):
    onkapis = input("mis sul kapis")
    if onkapis == "ei":
        kapis = False
    else:
        kapis=True
        print("saab ühepajatoitu teha")
        Miskapis =onkapis

if (kasonvett and kasonpott):
    print ("saad teha keedetud vett")
    
if(kartul and puljong):
    print("saad hautist teha")



            