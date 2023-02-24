import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

answer = messagebox.askquestion("Question", "Hello, how are you? Yes / No ?")

if answer == 'yes':
    print("The user clicked 'Yes'.")
else:
    print("The user clicked 'No'.")

exit()
