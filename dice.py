import random

dn1=random.randint(1,12)
dn2=random.randint(1,min(dn1,9))
dn3=random.randint(1,min(dn2,6))
    
attempts=9

print("Guess the number on all 3 dices to win the game.")
print("Numbers obtained can be from 1-12 for dice 1 , 1-9 for dice 2 and 1-6 for dice 3.")
print("Numbers obtained on subsequent dices can't be greater than the numbers obtained by the previous dices.")

g1=g2=g3=0

def guess_compare(n,c):
    if(c==0):
        c=3
    global attempts
    print("Attempts remaining : ",attempts,end="\t")
    global g1,g2,g3
    if(g1):
        print(" , Dice 1 => ",dn1,end="\t")
    if(g2):
        print(" , Dice 2 => ",dn2,end="\t")
    if(g3):
        print(" , Dice 3 => ",dn3,end="\t")

    print("\nGuess the number obtained on Dice",c)
    g=int(input("Guess=>"))
    attempts-=1
    if(n==g):
        print("Dice ",c,": Correct Guess.")
        if(c==1):
            g1=1
        elif(c==2):
            g2=1
        else:
            g3=1
    elif(n>g):
        print("Dice ",c,": The guess was smaller.")
    else:
        print("Dice ",c,": The guess was greater.")

cc=1
dnlist=[dn3,dn1,dn2]
while attempts:
    glist=[g3,g1,g2]
    cc%=3
    cc+=glist[cc]
    if(not glist[cc]):
        guess_compare(dnlist[cc],cc)
    cc+=1
    if(g1 and g2 and g3):
        print("Congrats !!!! You won the game with",attempts,"attempts remaining. The numbers were ",dn1,dn2,dn3,"respectively.")
        break
    elif(not attempts):
        print("Better luck next time. The numbers were ",dn1,dn2,dn3,"respectively.")
