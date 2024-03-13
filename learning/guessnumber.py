# Game -> guess the number
import random

random_num = random.randint(1,25)
intents = 0

print("Guess the nummer. You can try 5 times.")

while intents < 5:
    print(f'Intentos', {intents})

    intent = int(input())
    intents += 1

    if intent < random_num:
        print("Too low")
    elif intent > random_num:
        print("Too much")
    elif intent == random_num:
        break

if intent == random_num:
    print(f'Congrats, u guess the number:', {random_num})
else:
    print(f"Sorry, u lost. The number was: ",random_num)