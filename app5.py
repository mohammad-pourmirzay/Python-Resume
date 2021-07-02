import random

bot_input = random.choice(["Lion", "Line"])

while True:
    user_input = input("(Lion, Line)>> ").lower()
    if user_input == "lion" or user_input == "line":
        break
    else:
        print("Enter only (lion or line)")


if bot_input == "Lion":
    if user_input == "Lion":
        print("Your Win!!!")
        print(bot_input)
    else:
        print("Your Lost!!!")
        print(bot_input)
else:
    if user_input == "Line":
        print("Your Win!!!")
        print(bot_input)
    else:
        print("Your Lost!!!")
        print(bot_input)