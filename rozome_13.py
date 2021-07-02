from math import sqrt
while True:
    user_calculation_type = input("""Hello! Welcome to the program that 
takes the side of a right triangle with the help of the Pythagorean relation! 
You want to get the chord side or the adjacent sides of 
the chord. Please enter only the chord and the adjacent side 
(Chord, Adjacent to chord): """).capitalize()
    if user_calculation_type == "Chord":
        first_side_adjacent_to_chord = int(input("Please enter only the value of the side adjacent to the chord Example (5): "))
        second_value_of_side_adjacent_to_chord = int(input("Please enter only the value of the second side adjacent to the chord Example (12): "))
        second_power_of_first_side_adjacent_to_chord = first_side_adjacent_to_chord ** 2
        second_power_of_second_side_adjacent_to_chord = second_value_of_side_adjacent_to_chord ** 2
        add_two_values = second_power_of_first_side_adjacent_to_chord + second_power_of_second_side_adjacent_to_chord
        radical_values = sqrt(add_two_values)
        print(f"The chord side is unknown {radical_values}")
        break
    elif user_calculation_type == "Adjacent to chord":
        chord_input = int(input("Just enter the chord value of the right triangle Example (13): "))
        input_on_side_adjacent_to_chord = int(input("Enter only the value of the side adjacent to the chord Example (5): "))
        power_of_two_chords = chord_input ** 2
        power_of_twe_Adjacent_side_chord = input_on_side_adjacent_to_chord ** 2
        minus_two_values = power_of_two_chords - power_of_twe_Adjacent_side_chord
        radical_values = sqrt(minus_two_values)
        print(f"The unknown value of the adjacent side of the chord is {radical_values}")
        break
    else:
        print("Again!!!")
