#Fruit images by GameSupplyGuy on itch.io

from tkinter import *
import random

window = Tk()
window.title('The fruit Monster Game')

canvas = Canvas(window, width=400, height=400, bg = 'black')
canvas.pack()

title = canvas.create_text(200, 200, text= 'The fruit Monster',fill='white', font = ('Helvetica', 30))
directions = canvas.create_text(200, 300, text= 'Collect fruit but \n watch out for the peanuts!', fill='white', font = ('Helvetica', 20))

score = 0
score_display = Label(window, text="Score: " + str(score))
score_display.pack()

level = 1
level_display = Label(window, text="Level: " + str(level))
level_display.pack()

player_image = PhotoImage(file="greenChar.gif")
mychar = canvas.create_image(200, 360, image = player_image)

fruit_list = [] 
peanut_list = [] 
fruit_speed = 2
fruit_file_list = [PhotoImage(file="Fruits\\peanut.gif"), PhotoImage(file="Fruits\\apple.gif"), PhotoImage(file="Fruits\\banana.gif"), PhotoImage(file="Fruits\\cherry.gif"), PhotoImage(file="Fruits\\orange.gif"), PhotoImage(file="Fruits\\pear.gif"), PhotoImage(file="Fruits\\grape.gif"), PhotoImage(file="Fruits\\strawberry.gif")]

# make fruit at random places
def make_fruit():
    xposition = random.randint(1, 400)
    rand_fruit = random.randint(0, len(fruit_file_list)-1)
    fruit = canvas.create_image(xposition, 0, image = fruit_file_list[rand_fruit])
    fruit_list.append(fruit)
    if rand_fruit == 0:
        peanut_list.append(fruit)
    window.after(1000, make_fruit)
    
# move fruit downwards
def move_fruit():
    for fruit in fruit_list:
        canvas.move(fruit, 0, fruit_speed)
        if canvas.coords(fruit)[1] > 400:
            xposition = random.randint(1,400)
            canvas.coords(fruit, xposition, 0)
    window.after(50, move_fruit)


# update score, level and fruit_speed
def update_score_level():
    global score, level, fruit_speed
    score = score + 1
    score_display.config(text="Score: " + str(score))
    if score > 5 and score <= 10:
        fruit_speed = fruit_speed + 1
        level = 2
        level_display.config(text="Level: " + str(level))
    elif score > 10:
        fruit_speed = fruit_speed + 1
        level = 3
        level_display.config(text="Level: " + str(level))
    
def end_game_over():
    window.destroy()
    
def end_title():
    canvas.delete(title) 
    canvas.delete(directions) 

# check distance between 2 objects - return true if they 'touch'
def collision(item1, item2, distance):
    xdistance = abs(canvas.coords(item1)[0] - canvas.coords(item2)[0])
    ydistance = abs(canvas.coords(item1)[1] - canvas.coords(item2)[1])
    overlap = xdistance < distance and ydistance < distance
    return overlap

def check_hits():
    for fruit in peanut_list:
        if collision(mychar, fruit, 60):
            background = canvas.create_rectangle(0, 0, 400, 400, fill="black")
            game_over = canvas.create_text(200, 200, text= 'Game Over', fill='red', font = ('Helvetica', 30))
            canvas.create_text(200, 300, text= "Score: "+str(score), fill='white', font = ('Helvetica', 30))
            window.after(2000, end_game_over)
            return
    for fruit in fruit_list:
        if collision(mychar, fruit, 60):
            canvas.delete(fruit)
            fruit_list.remove(fruit)
            update_score_level()
    window.after(100, check_hits)

move_direction = 0
def check_input(event):
    global move_direction
    key = event.keysym
    if key == "Right":
        move_direction = "Right"
    elif key == "Left":
        move_direction = "Left"
        
# handles when user stop pressing arrow keys
def end_input(event):
    global move_direction
    move_direction = "None"
    
def move_character():
    if move_direction == "Right" and canvas.coords(mychar)[0] < 400:
        canvas.move(mychar, 10,0)
    if move_direction == "Left" and canvas.coords(mychar)[0] > 0 :
        canvas.move(mychar, -10,0)
    window.after(16, move_character) 

canvas.bind_all('<KeyPress>', check_input)
canvas.bind_all('<KeyRelease>', end_input)

window.after(1000, end_title)
window.after(1000, make_fruit)
window.after(1000, move_fruit)
window.after(1000, check_hits)
window.after(1000, move_character)

window.mainloop()