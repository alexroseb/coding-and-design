from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox 
import random

window = Tk()
window.title('Recycling Game')
window.geometry("400x400")

style = Style(window)
style.theme_use('xpnative')

instruct = Label(window, text="What should you do with this item?")
instruct.pack()

objects = [PhotoImage(file='imgs\\chipbag.gif'), PhotoImage(file='imgs\\styrofoam.gif'), PhotoImage(file='imgs\\lightbulb.gif'), PhotoImage(file='imgs\\box.gif'), PhotoImage(file='imgs\\soupcan.gif'), PhotoImage(file='imgs\\utensils.gif')]
originalO = objects.copy()
total = len(objects)
answers = ["t", "c", "c", "r", "r", "t"]
originalA = answers.copy()

itemChoice = random.randint(0,len(objects)-1)
objChoice = objects.pop(itemChoice)
answerChoice = answers.pop(itemChoice)
pic = Label(window, image=objChoice)
pic.pack()

score = 0
score_display = Label(window, text="Score: " + str(score))
score_display.pack()

def reset():
    global score, objects, answers
    score = 0
    objects = originalO.copy()
    answers = originalA.copy()
def scoring(user_choice, answer):
    global score, itemChoice, objChoice, answerChoice
    if user_choice == answer:
        score += 1
        tkinter.messagebox.showinfo("Correct", "Correct! Good job.")
    elif answer == "t":
        tkinter.messagebox.showerror("Incorrect", "Sorry, you were incorrect. That should be trash.")
        reset()
    elif answer == "r":
        tkinter.messagebox.showerror("Incorrect", "Sorry, you were incorrect. That should be recycled.")
        reset()
    elif answer == "c":
        tkinter.messagebox.showerror("Incorrect", "Sorry, you were incorrect. That should be brought to the recycling center.")
        reset()
    score_display.config(text="Score: "+str(score))
    if score >= total:
        close = tkinter.messagebox.askyesno("Continue?", "Congratulations, you correctly identified all the items. Would you like to play again?")
        if close:
            reset()
        else:
            window.destroy()
    score_display.config(text="Score: "+str(score))
    itemChoice = random.randint(0,len(objects)-1)
    objChoice = objects.pop(itemChoice)
    answerChoice = answers.pop(itemChoice)
    pic.config(image=objChoice)

def scoringTrash():
    scoring("t", answerChoice)
def scoringRecycle():
    scoring("r", answerChoice)
def scoringCenter():
    scoring("c", answerChoice)

Button(window, text="Trash", command=scoringTrash).pack()
Button(window, text="Curb recycling", command=scoringRecycle).pack()
Button(window, text="Bring to the recycling center", command=scoringCenter).pack()

window.mainloop()