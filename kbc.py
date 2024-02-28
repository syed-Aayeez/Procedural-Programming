print("WLECOME TO THE GAME")
print("KOUN-BANEGA-CROREPATI")
questions=[
    ["who is mark zuker berg?", "aayeez", "founder of FB", "animal", "girl", 2],["who is elon musk?", "aayeez", "founder of tesla", "animal", "girl", 2],["who is bill gates ?", "aayeez", "founder of microsoft", "animal", "girl", 2],["who is steve jobs?", "aayeez", "founder of APPLE", "animal", "girl", 2],["who is thomas edison?", "aayeez", "founder of bulb", "animal", "girl", 2],["who is charles babbge?", "aayeez", "founder of COMPUTER", "animal", "girl", 2],["who is albert enstien?", "aayeez", "Scientist", "animal", "girl", 2],["who is mahatma gandhi?", "aayeez", "freedom fighter", "animal", "girl", 2],["who is ajay nagar?", "aayeez", "carryminati", "animal", "girl", 2],["who is supreme leader?", "aayeez", "samay raina", "animal", "girl", 2],["who is srk?", "aayeez", "actor", "animal", "girl", 2],["who is the iron man?", "aayeez", "tony stark", "animal", "girl", 2],["who is tony star?", "aayeez", "iron man", "animal", "girl", 2],["who is chris hemsoworth?", "aayeez", "thor", "animal", "girl", 2],["who is thor?", "aayeez", "chris hemsworth", "animal", "girl", 2],["who is caption america?", "aayeez", "the one with shield", "animal", "girl", 2],["who is the one with with shield?", "aayeez", "caption america", "animal", "girl", 2],["who is the wonder woman ?", "aayeez", "gal gadot", "animal", "girl", 2],["who is gal gadot?", "aayeez", "wonder women", "animal", "girl", 2],["who is aayeez?", "aayeez", "human", "animal", "girl", 2]
    ]
levels=[1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
    print(f"Questions for Rs. {levels[i]}")
    print(f"{questions[i][0]}")
    print(f"a. {questions[i][1]}         b. {questions[i][2]}")
    print(f"c. {questions[i][3]}         d. {questions[i][4]}") 
    reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
    if (reply == 0):
        print("thankyou for playing")
        break
    if(reply ==2):
        print(f"CORRECT ANSWER!! YOU WON {levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
    else:
        print("WRONG ANSWER!!")
        break    
print(f"you take home {money}")    
