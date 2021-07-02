import termcolor
import os

print(termcolor.colored("I Live Python", color="red"))
print(termcolor.colored("I Live Python", color="blue"))

print()

print(termcolor.colored("I Live Python", on_color="on_red"))
print(termcolor.colored("I Live Python", on_color="on_blue"))

print()

print(termcolor.colored("I Live Python", attrs=["bold"]))
print(termcolor.colored("I Live Python", attrs=["dark"]))

os.system("notepad")
