print("welcome")
while True:
    helpp = input("Do you want help?(Yes, No): ").capitalize()
    if helpp == "Yes":
        print("""
First number
Four main operations (+, -, *, /)
Example(3+3=4, 3-3=0, 3*3=6, 3/3=1)
Second number
""")
        break
    elif helpp == "No":
        print()
        break
    else:
        print()
        print("Please only enter (Yes, No)")
        print()

first_number = int(input("First number: "))
print()
while True:
    four_main_actions = input("Four main actions(+, -, *, /): ")
    print()
    if four_main_actions == "+" or four_main_actions == "-" or four_main_actions == "*" or four_main_actions == "/":
        break
    else:
        print("Please only four actions enter namely(+, -, *, /)")
        print()
second_number = int(input("Second number: "))
print()

equal_sign = "="
if four_main_actions == "+":
    answer = first_number + second_number
    print(first_number, four_main_actions, second_number, equal_sign, answer)
elif four_main_actions == "-":
    answer = first_number - second_number
    print(first_number, four_main_actions, second_number, equal_sign, answer)
elif four_main_actions == "*":
    answer = first_number * second_number
    print(first_number, four_main_actions, second_number, equal_sign, answer)
else:
    answer = first_number / second_number
    print(first_number, four_main_actions, second_number, equal_sign, answer)


