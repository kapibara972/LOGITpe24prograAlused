# NB! kõik küsimised on tsüklis mis kontrollitud tsüklimuutujaga (mitte True ja break)
# NB! kõik sisendud töödeldakse standardkujule
#kirjuta programm mis
#
# küsib kasutajalt kas tal on perekonnaliikmeid
# - kui jah, siis küsib nende kõikide liikmete lemmikloomanimesid
# - kui ei, siis küsib kas kasutajal on lemmikloomi
# - - kui jah, siis küsib kõiki nimesid
# - - kui ei, siis ütleb kahju, pesaleidjas on palju kasse kes tahaksid kodu.
# programm väljastab lause, kus loetletakse kõik lemmikLoom, lemmikLoome puudumisel seda sammu ei tehta



onLiige = input("Kas sul on perekonnaliikmeid")
liige = []

while onLiige == "jah":
    nimi = input("Sisesta perekonnaliikme nimi: ")
    nimi =[]
    
    onLoom = input("Kas on lemmikloomi? (jah/ei): ")
    lemmikLoom = []
    
    while onLoom == "jah":
        loomNimi = input("Sisesta lemmiklooma nimi: ")
        lemmikLoom.append(loomNimi)
        onLoom = input("Kas tal on veel lemmikloomi? (jah/ei): ")
    
    liige.append((nimi, lemmikLoom))
    onLiige = input("Kas sul on veel perekonnaliikmeid? (jah/ei): ")


if len(liige) == 0:
    onLoom = input("Kas sul on lemmikloomi? (jah/ei): ")
    lemmikLoom = []
    
    while onLoom == "jah":
        loomNimi = input("Sisesta lemmiklooma nimi: ")
        lemmikLoom.append(loomNimi)
        onLoom = input("Kas sul on veel lemmikloomi? (jah/ei): ")


if len(liige) > 0:
    print("Perekonnaliikmete lemmikLoom:")
    for liigeNimi, loomNimi in liige:
        print(liigeNimi,loomNimi,)
elif len(lemmikLoom) > 0:
    print("Kasutaja lemmikLoom:")
    print(lemmikLoom)
else:
    print("Kahju, pesaleidjas on palju kasse, kes tahaksid kodu.")