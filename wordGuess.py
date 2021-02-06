import random

def hangman():
    words=["little","greater","smaller","college","school","books","ticks","father","mother","brother"]
    word=words[random.randint(0,len(words)-1)]
    valid="qwertyuiopasdfghjklzxcvbnm"
    turns=10
    ans=""
    guess=""
    while len(word) and turns:
        show=""
        for x in word:
            if x in ans:
                show+=x
            else:
                show+="_ "
        if show==word:
            print("You Win !!! The word was ",show,".\t Attempts left :",turns,"Wrong attempts :",10-turns)
            break
        print("Guess the word : ",show,"\t Attempts left :",turns,"Wrong attempts :",10-turns)
        guess=input()
        
        if guess in valid:
            ans+=guess
        else:
            print("Enter a valid character.")
            guess=input()
        if guess not in word:
            turns-=1
        if turns==10:
            print("You Lose.")
            break

print("Welcome to the Game !!\nEnter your name : ",end=" ")
name=input()
print("-----"*15)
print("Welcome",name,"you have 10 wrong guess remaining for guessing the word.")
hangman()
