import random
list = ['rock', 'paper', 'scissors']
com_inp = random.choice(list)
print("GAME")
print("ROCK - PAPER - SCISSORS")
user_inp = input("Enter your choice : ")
print(com_inp)
if user_inp == 'rock' and com_inp == 'scissors' : 
    print("you win")
elif user_inp == 'rock' and com_inp ==  'paper' :
    print("computer wins")
elif user_inp == 'scissors' and com_inp == 'paper' : 
    print("you win")
elif user_inp == 'scissor' and com_inp == 'rock' :   
    print("computer wins")
elif user_inp == 'paper' and com_inp == 'rock' :
    print("you win")
elif user_inp == 'paper' and com_inp == 'scissors' : 
    print("computer wins ")
else:  
    print("its tie") 