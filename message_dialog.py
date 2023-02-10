import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

answer = messagebox.askquestion("Question", "How is your day? Fine, Yes / No ?")

if answer == 'yes':
    print("The user clicked 'Yes'.")
else:
    print("The user clicked 'No'.")

exit()
