# kirjuta programm mis
# küsib kasutajalt kui suur ta põrand on
# (selle jaoks on vaja ristküliku valemit kasutada, ning küsida kasutajalt a ja b külg sentimeetrites)
# küsib kasutajalt milliseid põrandaplaate ta tahab
# kasutajale antakse 6 ascii näidet, ja kasutaja sisestab numbri milline muster talle meeldib
#
# ██░░ ║┌─┐ ▀▄░░
# ░░██ ║└─┘ ░░▀▄ (muid mustreid saab välja mõelda kas tähtedest või start -> character map abiga)
# (ülejäänud kolm mustrit mõtle ise)
# väljasta kasutajale ekraan mustriga koos hinnaarvutusega.
# (esimene muster on odavaim, viimane kalleim, tehe on pindala*mustriväärtus)
# küsi kas kasutaja maksab või mitte
# kui ei maksa, alanda hinda 10% ja küsi uuesti
# kui ei maksa, alanda hinda veel samapalju ja ütle viimane hind

print("mõõda põranda suurused cm, kui mõõtsid ära kirjuta ok")
ok = input()
print(" ütle pikkus")
pikkus = int(input())
print (" ütle laius")
laius = int(input())

pindala = pikkus * laius


print (" vali milline 1-6")
print (" 1.")
print(" ██░░\n ║┌─┐\n ▀▄░░\n")

print ("2.")
print (" ░░██\n ║└─┘\n ░░▀▄\n")

print("3.")
print(" ░░▀▄\n ███▒\n ▒▒▒░\n")

print("4.")
print(" ▒▒▒█\n ░░░░\n ░░░░\n")

print("5.")
print (" ░▒▒▒\n ██▒▒\n ▒▒░░\n")

print("6.")
print (" ▒▒██\n ░░░░\n ▒▒░░\n")

valik = int(input())
plaadihind = 0

if ( valik == 1):
    print (" ██░░\n ║┌─┐\n ▀▄░░")
    print("maksab 100 ")
    plaadihind = 100
    
if ( valik == 2):
    print (" ░░██\n ║└─┘\n ░░▀▄\n")
    print("maksab 200 ")
    plaadihind = 200
    
if ( valik == 3):
    print (" ░░▀▄\n ███▒\n ▒▒▒░\n")
    print("maksab 300 ")
    plaadihind = 300
    
if ( valik == 4):
    print (" ▒▒▒█\n ░░░░\n ░░░░\n")
    print("maksab 400 ")
    plaadihind =400
    
if ( valik == 5):
    print (" ░▒▒▒\n ██▒▒\n ▒▒░░\n")
    print("maksab 500 ")
    plaadihind =500
    
if ( valik == 6):
    print (" ▒▒██\n ░░░░\n ▒▒░░\n")
    print("maksab 600 ")
    plaadihind =600
    
if (valik > 6):
    print (" sellist variant polnud")
    
kokkuMaks = pindala * plaadihind

print(" kokku läheb" ,kokkuMaks,)
print(" olete valmis maksta")
valmis = input()

if ( valmis == "ei"):
    print ("siis teeme soodustuse 10%")
    soodustusUks = kokkuMaks * 0.9
    print (" hind on siis" ,soodustusUks,)
    print (" maksad? ")
    valmisKaks = input()
    
    if ( valmisKaks == "ei"):
        print (" viimane pakkumine -10%")
        soodustusKaks = soodustusUks * 0.9
        print (" hind on" ,soodustusKaks,)
        print (" maksad?")
        maksadKolm = input
        
        if ( maksadKolm =="ei"):
            print(" siis tõmba minema")
            
        else:
            print (" maksa, hind on" ,soodustusKaks,)
          
    else:
        print(" maksa")
    
else:
    print (" MAKSA SIIS")






