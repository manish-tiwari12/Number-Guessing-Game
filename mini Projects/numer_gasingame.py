import random 

user = -1
computer = random.randint(1,100)
atemp = 1

while (user != computer):
    user = int(input("Enter Your Number: "))
    if user > computer:
        print("Enter Small Number")
    elif user < computer:
        print("Enter Highe Number")
    atemp += 1 


print(f"You hav guessed the number  {computer} courruntly in {atemp} attempt")

