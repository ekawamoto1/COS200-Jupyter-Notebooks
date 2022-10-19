# https://stackoverflow.com/questions/29158220/tkinter-understanding-mainloop
# https://stackoverflow.com/questions/11303200/python-tkinter-loop-in-label
#
# Exercises:
# 1. Write a UDF set_to_string() that converts a set (of strings) to a comma-separated string
# 2. Fix a bug by modifying phrase_so_far() to check if a letter has been guessed before so that
#    no money is awarded
# 3. Write a UDF spin_wheel() that returns an integer that is a dollar amount, or 0 (lose turn), or -1 (bankrupt)
# 4. Add labels to display spin, amount, and the number of occurrences of letter that the player guesses
# 5. Change logic to make player pay $100 to guess a vowel ("buy a vowel"), no matter how many times it occurs in word
#
# Extra challenges (do any or all of these):
# 6. Add ability to read phrases from a text file
# 7. Add a "You win!" message if the player gets all the letters without losing a turn or going bankrupt on the last guess
# 8. Add rot13() function to encrypt/decrypt phrase (https://en.wikipedia.org/wiki/ROT13)
# 9. Add something of your own choosing (colors, sound effects, etc.)
#

from tkinter import *           # package of Python Tk widgets (graphical user interface elements)
from tkinter import ttk         # "themed" Tk widgets (better look and feel across platforms)
import random as rnd


# When a letter is guessed, this UDF checks it against the phrase
# then reveals the positions of that letter in the phrase if it occurs in the phrase
# returns a list with the phrase whose letters have been revealed so far
# and the number of occurrences of the letter in the phrase (negative if a vowel)
# it also updates inSet by adding the letter that was guessed
def phrase_so_far(letter, inPhrase, inSet) -> list:
    phraseToDisplay = ""
    letterOccurrenceCount = 0
    punct = [" ", ",", ".", "?", "!"]
    vowels = ["a", "e", "i", "o", "u"]

    if letter in inPhrase:
        for char in inPhrase:
            if char == letter:
                letterOccurrenceCount += 1
    if letter in vowels:
        letterOccurrenceCount *= -1

    inSet.add(letter)

    for char in inPhrase:
        if char in punct:
            phraseToDisplay += char
        elif char in inSet:
            phraseToDisplay += char
        else:
            phraseToDisplay += "*"

    outList = [phraseToDisplay.upper(), letterOccurrenceCount]
    return outList


# Converts the set of guessed letters to a string of uppercase letters
def set_to_string(inSet) -> str:
    pass


# Global variable that keeps track of how much money you have so far
myWinnings = 0


# The main application
def main():
    phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
    guessedLetters = set()  # creates an empty set; {} creates an empty dictionary
    global myWinnings

    window = Tk()
    # https://www.askpython.com/python-modules/tkinter/stringvar-with-examples
    displayPhrase = StringVar()
    displayLetters = StringVar()


    displayPhrase.set(phrase)
    displayLetters.set(set_to_string(guessedLetters))

    # https://www.pythontutorial.net/tkinter/tkinter-label/
    lbl1  = ttk.Label(window, text="Enter a letter: ")
    lbl2a = ttk.Label(window, text="Letters already entered: ")
    lbl3a = ttk.Label(window, text="Unknown phrase so far: ")
    lbl4a = ttk.Label(window, text="Wheel spin: ")
    lbl4c = ttk.Label(window, text="Number of occurrences: ")
    lbl5a = ttk.Label(window, text="Your total so far: ")

    # https://www.pythontutorial.net/tkinter/tkinter-entry/
    t1 = ttk.Entry()

    # Updates labels on output window
    def update_label():
        global myWinnings
        letter = t1.get()
        # clears the entry box
        t1.delete(0, 'end')

        # updates guessedLetters with the new letter that was guessed
        newList = phrase_so_far(letter, phrase.lower(), guessedLetters)

        showGuessedLetters = set_to_string(guessedLetters)   # string containing letters already guessed
        displayLetters.set(showGuessedLetters)

        phraseToDisplay = newList[0]      # the phrase revealing successfully guessed letters so far
        displayPhrase.set(phraseToDisplay)

        occurrenceCount = newList[1]      # the number of times letter occurs in the phrase


        print(phraseToDisplay + ": " + letter.upper(), 'occurs', occurrenceCount, 'times')

        spinResult = spin_wheel()
        print('result of wheel spin:', spinResult)

        if spinResult < 0:        # bankrupt: myWinnings is zeroed out
            myWinnings = 0
        else:                     # adds to myWinnings
            myWinnings += spinResult * occurrenceCount

        print('my winnings so far:', myWinnings, '\n')


        window.update()

    # Spins the wheel, and returns a monetary amount, 0 (lose a turn), or -1 (bankrupt)
    def spin_wheel() -> int:
        pass


    # https://www.pythontutorial.net/tkinter/tkinter-button/
    b1 = ttk.Button(window, text="Guess", command=update_label)
    b1.pack()

    # this only runs once to initialize the displayed phrase
    myList = phrase_so_far("", phrase.lower(), guessedLetters)
    initialStr = myList[0]
    displayPhrase.set(initialStr)
    showGuessedLetters = set_to_string(guessedLetters)
    displayLetters.set(showGuessedLetters)

    # update labels on output window with text to display
    lbl2b = ttk.Label(window, textvariable=displayLetters, font=("Courier", 14, "bold"))
    lbl3b = ttk.Label(window, textvariable=displayPhrase, font=("Courier", 14, "bold"))
    # set up labels lbl4b, lbl4d, and lbl5b corresponding to labels lbl4a, lbl4c, and lbl5a above



    # set positions of labels, text entry box, and button on output window
    dx = -10
    dy = -2
    lbl1.place(x=20, y=20)
    t1.place(x=150, y=15)
    lbl2a.place(x=20, y=60)
    lbl2b.place(x=180+dx, y=60+dy)
    lbl3a.place(x=20, y=100)
    lbl3b.place(x=180+dx, y=100+dy)
    lbl4a.place(x=20, y=140)

    lbl4c.place(x=250, y=140)

    lbl5a.place(x=20, y=180)

    b1.place(x=325, y=220)

    # set title and size of output window
    window.title('Wheel of Fortune')
    window.geometry("825x260+5+5")
    window.resizable(False, False)

    # https://realpython.com/python-gui-tkinter/
    window.mainloop()
    print("Thanks for playing ... goodbye!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()