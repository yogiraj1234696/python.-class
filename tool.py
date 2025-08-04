import random
guess=int(input("enter the number"))
number=random.randint(1,10)
if(guess==number):
    print("congratulation you won 20% discount")
else:
     print("better luck next time")
