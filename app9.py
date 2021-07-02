import webbrowser
from tkinter import *

root = Tk()

root.title("Web_Browser")
root.geometry("300x200")

def google():
    webbrowser.open("www.google.com")

my_google = Button(root, text="open google", command=google).pack(pady=20)

root.mainloop()
