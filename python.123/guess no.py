import random
x = random.randint(1,9)
guess = 0
print("guess no:")
while guess!= x:
    guess = int(input("guess: "))
    if guess!= x:
        print("wrong answer")
    else:
        print("correct")
