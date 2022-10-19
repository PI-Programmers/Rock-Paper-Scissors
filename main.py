import random
print("Instructions ---")
print("Enter R for rock.")
print("Enter P for paper.")
print("Enter S for scissor.")
print("Enter E to end the game.")
i=1
h=0
c=0
while i!=0:
    v=random.randint(1,3)
    if(v==1):
        t="R"
    elif(v==2):
        t="P"
    else:
        t="S"
    a=input("Choose what you want to throw--")
    if(a=="R"or a=="P"or a=="S"):
        if(a==t):
            print("Both you and computer choose", a, "!")
        elif(a=="R" and t=="P"):
            print("Computer plays",t,". You lose! Try again.")
            c+=1
        elif(a=="P" and t=="R"):
            print("Computer plays",t,". You win!")
            h+=1
        elif(a=="R" and t=="S"):
            print("Computer plays",t,". You win!")
            h+=1
        elif(a=="S" and t=="R"):
            print("Computer plays",t,". You lose! Try again.")
            c+=1
        elif(a=="S" and t=="P"):
            print("Computer plays",t,". You win!")
            h+=1
        elif(a=="P" and t=="S"):
            print("Computer plays",t,". You lose! Try again.")
            c+=1
    elif(a=="E"):
        print("The game is ended, thanks for playing.")
        print("Your score is ->",h, "and the computer's score is -> ",c)
        if(h>c):
            print("Great Game!Well Played!")
        else:
            print("Better luck next time!")
        i=0
    else:
        print("Invalid input, try again.")
        
    
    
