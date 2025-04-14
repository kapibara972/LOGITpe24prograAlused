
# NB! kasutajalt sisendi võtmine peab igal juhul tsüklis olema niikaua kuni programm saab õige sisendi
# NB! kasutajasisend tuleb töödelda standardkujuke, nime puhul esisuurtäht, programmi jaoks vajalik sisend ühtlasele kujule jne
# kirjuta programm mis
#
# küsib kasutajalt kui vana ta on
# küsib kasutajalt kui pikk ta on meetrites
# küsib kasutajalt tema ees ja perekonnanime
# küsib kasutajalt kas talle meeldivad geomeetrilised kujundid
# kui kasutaja vastab jah, siis küsitakse kasutajalt terve rida küsimusi järgnevate kujundite kohta: (ring, ruut, kolmnurk, ovaal)
# - kas talle meeldib <kujund>
# - kui kasutaja vastab <kujund>i kohta jah, siis peab programm meelde jätma et kasutaja tahab seda kujundit eraldi muutujas
# - kasutajalt küsitakse ka tema lemmikvärvi kohta, mille jaoks antakse kasutajale inglisekeelne valik
# - seejärel joonistab programm kõik kujundid mis said "jah" vastuse kasutaja lemmikvärviga ekraanile +
# - kujundite küljepikkus tuleb läbi korrutada kasutaja pikkusega. kujundite standardküljepikkus on 100px
# - Viimasena joonistatakse ekraanile teksti abil sõnum "palun"<kasutajanimi>"siin on sinu lemmikkujundid"<värv> värviga


from tkinter import*
raam= Tk()
raam.title(" i are windo")
tahvel=Canvas(raam, width=1000,height=1000)

vana=""
pikk=""
enimi=""
pnimi=""
geoküs=""
värv=""

#kujundid
ring=""
ruut=""
kolmnurk=""
ovaal=""

while(vana==""):
    vana= int(input("kui vana oled"))
    
while(pikk==""):
    pikk=float(input("kui pikk oled meetrites"))
    
while(enimi==""):
    enimi=input("ütle eeesnimi")

while(pnimi==""):
    pnimi=input("ütle perekpnna nimi")
    

while(geoküs==""):
    geoküs=input("kas meeldivad geo kujundid")
    if geoküs=="ei":
        print (" käi perkele")
        
while (ring==""):
    ring=input("meeldib ring").lower()
while (ruut==""):
    ruut=input("meeldib ruut").lower()
while (kolmnurk==""):
    kolmnurk=input("meeldib kolmnurk").lower()
while (ovaal==""):
    ovaal=input("meeldib ovaal").lower()
    
    
while(värv==""):
    värv=input("ütle värv in inka keeles")




if(ring=="jah"):
    tahvel.create_oval(pikk*100, pikk*100, pikk*300, pikk*300,outline=värv, fill=värv)
    tahvel.create_text(490,375,text=("palun",enimi,"siin on sinu lemmikkujundid",värv, "värviga"), fill=värv)
if(ruut=="jah"):
    tahvel.create_polygon(pikk*700,pikk*700,pikk*900,pikk*900,outline=värv, fill=värv)
    tahvel.create_text(490,375,text=("palun",enimi,"siin on sinu lemmikkujundid",värv, "värviga"), fill=värv)
if(kolmnurk=="jah"):
    tahvel.create_polygon(pikk*200,pikk*600,pikk*200,pikk*700,pikk*300,pikk*700,outline=värv, fill=värv)
    tahvel.create_text(490,375,text=("palun",enimi,"siin on sinu lemmikkujundid",värv, "värviga"), fill=värv)
if(ovaal=="jah"):
     tahvel.create_oval(pikk*600,pikk*600,pikk*700,pikk*900,outline=värv, fill=värv)
     tahvel.create_text(490,375,text=("palun",enimi,"siin on sinu lemmikkujundid",värv, "värviga"), fill=värv)
          



tahvel.pack()
raam.mainloop()

