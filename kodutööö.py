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
# kogu arvutamine peab toimuma loogiliste tehetega

while True:
    
    hapukapsas = input("Kas sul on hapukapsas? (jah/ei): ").lower()
    while hapukapsas != "jah" and hapukapsas != "ei":
        hapukapsas = input("Palun sisesta jah või ei - Kas sul on hapukapsas? (jah/ei): ").lower()

    pott = input("Kas sul on pott? (jah/ei): ").lower()
    while pott != "jah" and pott != "ei":
        pott = input("Palun sisesta jah või ei - Kas sul on pott? (jah/ei): ").lower()

    vesi = input("Kas sul on vett? (jah/ei): ").lower()
    while vesi != "jah" and vesi != "ei":
        vesi = input("Palun sisesta jah või ei - Kas sul on vett? (jah/ei): ").lower()

    kartul = input("Kas sul on kartulit? (jah/ei): ").lower()
    while kartul != "jah" and kartul != "ei":
        kartul = input("Palun sisesta jah või ei - Kas sul on kartulit? (jah/ei): ").lower()

    puljong = input("Kas sul on puljongit? (jah/ei): ").lower()
    while puljong != "jah" and puljong != "ei":
        puljong = input("Palun sisesta jah või ei - Kas sul on puljongit? (jah/ei): ").lower()

    kapis = input("Kas sul on midagi muud kapis? (jah/ei): ").lower()
    while kapis != "jah" and kapis != "ei":
        kapis = input("Palun sisesta jah või ei - Kas sul on midagi muud kapis? (jah/ei): ").lower()

    if hapukapsas == "jah" and pott == "jah" and vesi == "jah" and kartul == "jah" and puljong == "jah" and kapis == "ei":
        print("Sa saad teha hapukapsast.")
    elif hapukapsas == "ei" and pott == "jah" and vesi == "jah" and kartul == "jah" and puljong == "jah" and kapis == "ei":
        print("Sa saad teha hautist.")
    elif hapukapsas == "jah" and pott == "jah" and vesi == "jah" and kartul == "jah" and puljong == "jah" and kapis == "jah":
        print("Sa saad teha kõike: hapukapsast, hautist, ühepajatoitu, mulgikapsaid.")
    elif hapukapsas == "jah" and pott == "ei" and vesi == "jah" and kartul == "jah" and puljong == "jah" and kapis == "jah":
        print("Sa saad teha ühepajatoitu.")
    elif hapukapsas == "jah" and pott == "jah" and vesi == "ei" and kartul == "jah" and puljong == "jah" and kapis == "ei":
        print("Sa saad teha mulgikapsaid.")
    elif hapukapsas == "jah" and pott == "jah" and vesi == "jah" and kartul == "jah" and puljong == "ei" and kapis == "ei":
        print("Suppi teha ei saa.")
    else:
        print("Ei saa teha midagi sobivat.")

    break