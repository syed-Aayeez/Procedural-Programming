import string
import random
a=random.choice(string.ascii_letters)
b=random.choice(string.ascii_letters)
c=random.choice(string.ascii_letters)
d=random.choice(string.ascii_letters)
e=random.choice(string.ascii_letters)
f=random.choice(string.ascii_letters)
question_1=int(input("ENTER AS 1 TO ENCODE OR 2 TO DECODE:"))
if(question_1<2):
    print("lets ENCODE")
    question_2 =input("ENTER THE WORD TO BE ENCODED:")
    if (len(question_2)>=3):
        start = a + b + c
        end = d + e + f
        str = start + question_2[1:] + question_2[0] + end
        print(str)
    else:
        reverse = question_2[::-1]
        print(reverse)   
else:
    result=[]
    print("lets DECODE")
    question_3 =input("ENTER THE WORD TO BE DECODED:")
    if (len(question_3)>=3):
        removing = question_3[3:-3]
        removing =  removing[-1] + removing[:-1]
        result.append(removing)
        print(result)
    else:
        reverse_2 = question_3[::-1]
        print(reverse_2) 

    



