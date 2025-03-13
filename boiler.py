# kirjuta programm mis
# küsib kasutajalt kas ta soovib osta boilerit
# (selle jaoks on vaja risttahuka valemit kasutada, ning küsida kasutajalt a( laius ) ja b ( pikkus) külg oõhjapindala jaoks sentimeetrites ja olevasoleva ala kõrguse h (kõrgus))
# olenevalt olemasolevast ruumalast
# - kui ruumala on liiga väike, öeldakse et meil ei ole pakkuda midagi sellises suuruses
# - kui ruumala on väike aga sobiv, pakutakse väikest boilerit väikese hinnaga
# - kui ruumala on paras, siis pakutakse väikest boilerit ja parajast boilerit
# - kui ruumala on suur, siis pakutakse väikest, parajast ja suurt boilerit.
# - kasutajalt küsitakse millist boilerit ta osta soovib NIMEPIDI, programm peab tuvastama õige nime kasutades .lower() või .upper() meetodeid
# väikese boileri maht arvutada a=35 b=35 h=70
# paraja boileri maht arvutada a=45 b=45 h=90
# suure boileri maht arvutada a=60 b=60 h=210
# hinnad mõtlete ise välja
# küsi kas kasutaja maksab või mitte
# kui ei maksa, alanda hinda 10% ja küsi uuesti
# kui ei maksa, alanda hinda veel samapalju ja ütle viimane hind



print(" kas tahad boilerit")
vastus = input()
if (vastus == "jah"):
    print("ütle laius cm- des")
    Alaius = int(input())
    print("ütle pikkus ")
    Bpikkus = int(input())
    print (" ütle kõrgus ")
    Hkorgus = int(input())

    tahukas = Alaius*Bpikkus*Hkorgus
    
    vaikeBoil = 35*35*70
    keskBoil = 45*45*90
    suurBoil = 60*60*210
    
    
    if ( tahukas < vaikeBoil ):
        print (" sellist pole liiga väike")
    elif ( tahukas < keskBoil):
        print(" saan pakuda väiksemat")
        print(" millist valid")
        vali = input()
        if ( vali == "väike"):
            print ("bosh maksab 1000")
            maks = 1000
        if ( vali == "keskmine"):
            print (" nou neim maksab 2000")
            maks = 2000
        if ( vali == "suur"):
            print ("mitsu bishi maksab 4000")
            maks = 4000
        print (" olete valmis maksta võtta asjad")
        makstUks = input()
        print("võtta asjad")
        
        if ( makstUks == "ei"):
            print (" ok alandan hinda -10%")
            hind = maks * 0.9
            print (" maksab",hind,)
            print (" maksad")
            makstKaks = input()
              
            if ( makstKaks == "ei"):
                hindKaks = hind *0.9
                print (" viimane hind ori",hindKaks,)
            else:
                print(" tõmba minema ori")
        else:
            print(" tõmba minema")
    elif (tahukas < suurBoil):
        print(" suuremat pole")
        print(" millist valid")
        vali = input()
        if ( vali == "väike"):
            print ("bosh maksab 1000")
            maks = 1000
        if ( vali == "keskmine"):
            print (" nou neim maksab 2000")
            maks = 2000
        print (" olete valmis maksta võtta asjad")
        makstUks = input()
        
        if ( makstUks == "ei"):
            print (" ok alandan hinda -10%")
            hind = maks * 0.9
            print (" maksab",hind,)
            print (" maksad")
            makstKaks = input()
              
            if ( makstKaks == "ei"):
                hindKaks = hind *0.9
                print (" viimane hind ori",hindKaks,)
            else:
                print(" tõmba minema ori")
        else:
            print(" tõmba minema")
    elif ( tahukas > suurBoil):
        print(" pakun kõiki vali suur, keskmine ja väike ")
        print(" millist valid")
        vali = input()
        
        if ( vali == "väike"):
            print ("bosh maksab 1000")
            maks = 1000
        if ( vali == "keskmine"):
            print (" nou neim maksab 2000")
            maks = 2000
        if ( vali == "suur"):
            print ("mitsu bishi maksab 4000")
            maks = 4000
        print (" olete valmis maksta")
        makstUks = input()
        
        if ( makstUks == "ei"):
            print (" ok alandan hinda -10%")
            hind = maks * 0.9
            print (" maksab",hind,)
            print (" maksad")
            makstKaks = input()
              
            if ( makstKaks == "ei"):
                hindKaks = hind *0.9
                print (" viimane hind ori",hindKaks,)
                lõpp = input()
                if ( lõpp == "jah"):
                    print (" võtt asjad")
                    
                else:
                    print(" tõmba minema")
            else:
                print(" tõmba minema ori")
        else:
            print(" tõmba minema")
    
    

    
    
    
else:
    print (" tõmba nah... ")
             



        