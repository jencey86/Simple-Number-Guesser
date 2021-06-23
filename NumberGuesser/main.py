# imports tkinter for GUI stuff
import tkinter as tk
import random

# Create the window that gets displayed
window = tk.Tk()
window.title("Number Guesser")
window.geometry("600x400")

textLabel = tk.Label(text="I'm thinking of a number between 1 and 100", font=("Arial", 20, "bold"))
textLabel.pack()

guessLabel = tk.Label(text="Your guess: ")
guessLabel.pack()
guessInput = tk.Entry()
guessInput.pack()


def randomNumber():
    num = random.randrange(1, 100)
    return num


def numberCheck(num=randomNumber()):
    numGuess = int(guessInput.get())
    if num == numGuess:
        print("Good job!")
    elif num > numGuess:
        print("Your guess is too small! Try again")
    elif num < numGuess:
        print("Your guess is too high! Try again")


guessButton = tk.Button(text="Guess", bg="green", fg="white", command=numberCheck)
guessButton.pack()

window.mainloop()
