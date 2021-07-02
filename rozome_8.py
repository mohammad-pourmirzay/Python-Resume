name = str(input("Enter your name: "))
print(f"{name} you are stuck in a forest. Your task is to get out from the forest without dieing")
print("you are walking threw forest and suddenly a wolf comes in your way. now you have two options.")
print("1.run 2 climb the nearest tree")
while True:
    user = int(input("Choose one option 1 or 2: "))
    if user == 1:
        print("You Died!!")
        break
    elif user ==2:
        print("You survived!!")
        break
    else:
        print("Incorrect Input")
