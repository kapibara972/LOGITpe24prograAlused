# küsib kasutajalt tema pin koodi
# küsib kasutajalt tema isikukoodi
# kasutaja saab sisestada pin koodi ainult 3 korda
# kasutaja saab sisestada isikukoodi ka ainult 3 korda
# kui kasutaja on kõik korrad valesti sisestanud kas isikukoodi või pin koodi:
# - joonista kasutajale pilt, kus on kurb nägu trellide taga
# kui pinkood ja isikukood on õiged, küsi kasutajalt:
# - kas ta tahab raha välja võtta või oma pangakaarti tagasi
# - kui ta tahab raha välja võtta siis
# - - küsi kasutajalt kui palju ning joonista talle rahaleht mille peal on väljavõetud summa kirjutatud
# - kui ta tahab oma pangakaarti tagasi siis
# - - joonista talle pangakaart mille peal on tema isikukood
from tkinter import*

katsed=3
pin=1111
pink=0

katsed2=3
isikk=2222222222
isik=0


rahaSum=""

raam= Tk()
raam.title("sigma")
tahvel=Canvas(raam, width=1000,height=1000)

#  pin
while (katsed >0 and pin!=pink):
    pink=int(input("ütle pinkood"))
    katsed-=1
             
            
            
            
if(pink==pin):
    print("pin õige")
else:
    tahvel.create_oval(50, 50, 350, 350, fill="yellow", outline="black", width=2)
    tahvel.create_oval(120, 100, 180, 160, fill="black")  
    tahvel.create_oval(220, 100, 280, 160, fill="black")  
    tahvel.create_line(120, 260, 180, 260, width=5)  
    tahvel.create_line(220, 260, 280, 260, width=5)  
    tahvel.create_line(120, 260, 120, 270, width=5)  
    tahvel.create_line(280, 260, 280, 270, width=5)
    
    
    
#  isik
while (katsed2 >0 and isikk!=isik):
    isik=int(input("ütle isikukood"))
    katsed2-=1
    
if ( isik==isikk):
    print("isikukood õige")
else:
    tahvel.create_oval(50, 50, 350, 350, fill="yellow", outline="black", width=2)
    tahvel.create_oval(120, 100, 180, 160, fill="black")  
    tahvel.create_oval(220, 100, 280, 160, fill="black")  
    tahvel.create_line(120, 260, 180, 260, width=5)  
    tahvel.create_line(220, 260, 280, 260, width=5)  
    tahvel.create_line(120, 260, 120, 270, width=5)  
    tahvel.create_line(280, 260, 280, 270, width=5) 


if(pin==1111 and isik==2222222222):
    while(rahaSum==""):
        rahaSum=input("kas tahad raha välja või kaart tagasi. (välja/tagasi)")
    

#  raha välja   
    if(rahaSum=="välja"):
        raha=int(input("palju võttad välja"))
        tahvel.create_rectangle(20, 20, 580, 280, outline="green", width=5)
        tahvel.create_text(300, 50, fill="green")
        tahvel.create_text(300, 100, text="EURO",fill="green")
        tahvel.create_text(500, 250, text=raha,fill="green")
        tahvel.create_oval(150, 150, 250, 250, outline="green", width=3)  
        tahvel.create_oval(350, 150, 450, 250, outline="green", width=3)
       
       #kaart tagsi
    if(rahaSum=="tagasi"):
        tahvel.create_rectangle(50, 50, 550, 250, outline="blue", width=5)
        tahvel.create_oval(60, 60, 100, 100, outline="blue", width=5)
        tahvel.create_text(300, 100, text=isik,fill="black")
        tahvel.create_text(300, 150, text="Kehtiv kuni: 12/25",fill="black")
        tahvel.create_text(300, 200,fill="black")
        tahvel.create_text(500, 250, text="123",fill="black")
        
    




tahvel.pack()
raam.mainloop()