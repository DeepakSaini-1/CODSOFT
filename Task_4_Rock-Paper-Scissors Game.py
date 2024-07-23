from tkinter import messagebox
import tkinter as tk
import random


# main windows
# GUI 
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame = tk.Frame(root)
frame.grid(row=0, column=0, padx=20, pady=20)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

# create the buttons
Rock_button = tk.Button(frame, text="Rock", command=lambda: on_button_click('Rock'), height=2, width=10)
paper_button = tk.Button(frame, text="Paper", command=lambda: on_button_click('paper'), height=2, width=10)
Scissors_button = tk.Button(frame, text="Scissors", command=lambda: on_button_click('Scissors'), height=2, width=10)

# Creating and placing the result label
result_label = tk.Label(frame, text="Make your choice!", font=('Helvetica', 14))

# add buttons on the frmae 
Rock_button.grid(row=0, column=0, padx=10, pady=10)
paper_button.grid(row=0, column=1, padx=10, pady=10)
Scissors_button.grid(row=0, column=2, padx=10, pady=10)

# add the label show the winner
result_label.grid(row=1, column=0,columnspan=3, pady=20)



# Backend

def CompcompChoice():
    return random.choice(["Rock", "paper", "Scissors"])


def CheckWinner(user, comp):
    if user=="Rock" and comp=="paper" or user=="Scissors" and comp=="Rock" or user=="paper" and comp=="Scissors" :
        str=f"""
You chose:  {user}
Computer chose: {comp}

You lost!  {comp} beats your {user}"""

    elif comp =="Rock" and user=="paper" or comp =="Scissors" and user=="Rock" or comp =="paper" and user=="Scissors":
        str=f"""
You chose:  {user}
Computer chose: {comp}

You win!  Your {user} beats {comp}"""

    else:
        str=f"""
You chose:  {user}
Computer chose: {comp}

Game was Draw. Play again"""
    result_label.config(text=str)
    

def on_button_click(player_choice):
    CheckWinner(player_choice,CompcompChoice())

root.mainloop()