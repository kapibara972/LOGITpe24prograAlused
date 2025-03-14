#kiirjuta programm mis
# küsib kasutajalt tema lemmikvärv
# küsib kasutajalt tema lemmikkujund (ruut, ring, ristkülik, võrdhaarne kolmnutk, täisnurk kolmnurk)
# joonistab kasutajale vastava kujundi tema värvi
from turtle import*
from random import randint



print(" ütle lemmik värv, ütle inglise keeles")
varv = input()
print ("ütle lemmikmkujud (ruut, ring, ristkülik, võrdhaarne kolmnurk, täisnurkne kolmnurk)")
kujund = input()

if (kujund == "ruut"):
    color (varv)
    fd (100)
    lt(90)
    fd(100)
    lt(90)
    fd(100)
    lt(90)
    fd(100)
    
elif ( kujund =="ring"):
    color ( varv)
    begin_fill()
    circle(100)
    end_fill()

elif ( kujund =="võrdhaarne kolmnurk"):
    color (varv)
    fd(100)
    lt(120)
    fd(100)
    lt(120)
    fd(100)
    
    
elif ( kujund =="täisnurkne kolmnurk"):
    color (varv)
    fd(100)
    rt(120)
    fd(200)
    rt(150)
    fd(180)
elif (kujund =="ristkülik"):
    color(varv)
    fd(200)
    lt(90)
    fd(100)
    lt(90)
    fd(200)
    lt(90)
    fd(100)
    
    
    
exitonclick()




    
    
    
    
