	
# kirjuta programm mis
#
# küsib kasutajalt kas tal on kõht tühi.
# kui kasutaja vastab ei:
#---siis programm ütleb talle vastu tagasi "ootame teid jälle kui teil isu on"
# kui kasutaja vastab ja:
#---küsib programm kas ta tahab ise võileiva kokku panna, või lasta arvutil selle genereerida
#---kui kasutaja tahab ise kokku panna, siis:
#-------küsib programm temalt kas ta tahab ühepoolset võileiba või kahepoolset võileiba:
#-------küsib programm temalt kas ta tahab võileivale võid või majoneesi
#-------küsib programm temalt kas ta tahab kurki võileivale
#-------küsib programm temalt kas ta tahab tomatit võileivale
#-------küsib programm temalt kas ta tahab peekonit võileivale
#---kui kasutaja tahab suvaliselt kokku panna, siis genereeritakse talle 5 korda erinev võileiva osa järjest
#---programm koostab kasutajale ascii pildi erinevatest kihtidest mida kasutaja lisanud on või arvuti genereerinud on
#---, ja küsib temalt raha 1.50 + 0.75 iga lisatud kihi eest
#---kui kasutaja ei maksa, siis öeldakse talle "ootame teid jälle kui teil isu on ja raha ka"
#---kui kasutaja maksab, siis tagastatakse ascii võileib teatega "aitäh tellimuse eest, tulge jälle"
# sai - [ , ,, '' ']
# või ja majoneesi jaoks ei kuvata kihti, aga ta annab hinnas lihtsalt juurde
# kurk - ▄▄▄▄ ▄▄▄
#tomat - ( | ▌|██)
#bacon - "~-,._.,-~"~-,.

from random import randint
lisand = 0.75
summa =1.50
print(" on kõht tühi? ")
kohtTuh = input()

if (kohtTuh == "ei"):
    print(" siis tõmba minema ")
    
elif ( kohtTuh == "jah"):
    print( "kas valid ise või arvuti teeb")
    voileib = input()
    
    if (voileib == "ise"):
        print(" ühepoolne või kahepoolne")
        pool = input()
        if (pool == "ühe"):
            summa += 0.75
            
        print(" või, majonees")
        kreem = input()
        summa += 0.75
            
        print(" kurki")
        kurk = input()
        if (kurk == "jah"):
            summa += 0.75
            
        print(" tomatit ")
        tomat = input()
        if (tomat == "jah"):
            summa += 0.75
            
        print(" peekonit ")
        peekon = input()
        if (peekon == "jah"):
            summa += 0.75
        
        
        print ("kokku" ,summa,)
        
        
    elif ( voileib == "arvuti"):
        pool = randint ( 0,1)
        if pool == 1:
            summa += 0.75
            print (" sai- [ , ,, '' ']")
        kreem = randint ( 0,1)
        if kreem == 1:
            summa += 0.75
        kurk = randint ( 0,1)
        if kurk == 1:
            summa += 0.75
            print (" kurk -▄▄▄▄ ▄▄▄")
        tomat = randint ( 0,1)
        if tomat == 1:
            summa += 0.75
            print (" tomat- ( | ▌|██) ")
        peekon = randint ( 0,1)
        if peekon == 1:
            summa += 0.75
            print ("peekon- ~-,._.,-~~-,. ")
        
        print ("kokku" ,summa,)
    
        
    
        
                
                
    
                
    
