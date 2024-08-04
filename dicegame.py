import random 
import time

def roll_dice(n): 
    dice = [] # start with empty list of dice 
    # add random numbers between 1 to 6 to the list 
    for i in range(n): 
        dice.append(random.randint(1,6)) 
    return dice

def find_winner(cdice, udice): 
    computer_total = sum(cdice) 
    user_total = sum(udice) 
    if user_total > computer_total: 
        return "Congratulations, you win!"
    elif user_total < computer_total: 
        return "...Too bad, the computer won."
    else: 
        return 'It is a tie!'

def roll_again(choices, dice_list): 
    print('Rolling again...') 
    time.sleep(2) 
    for i in range(len(choices)): 
        if choices[i] == 'r': 
            dice_list[i] = random.randint(1,6)

def computer_strategy(n):
    time.sleep(2)
    choices = ''
    for i in range(n):
        if computer_rolls[i] <= 3:
            choices += "r"
        else:
            choices += "-"
    return choices

def computer_advanced(n):
    print("Computer is thinking...")
    if find_winner(computer_rolls, user_rolls) != "...Too bad, the computer won.":
        return computer_strategy(n)
    else:
        return "-"*n


#Start game
number_dice = int(input("Enter number of dice: "))
# User turn to roll 
time.sleep(2)
user_rolls = roll_dice(number_dice) 
print("User's first roll: ", user_rolls) 
# Computer's turn to roll 
print("Computer's turn. ") 
time.sleep(2)
computer_rolls = roll_dice(number_dice) 
print("Computer's first roll: ", computer_rolls)

reroll = input("Do you want to reroll any of your dice? y or n: ")
reroll_count = 0
while reroll == "y":
    user_choices = input("For each die, type - to hold or r to roll again: ") 
    # check length of user input 
    while len(user_choices) != number_dice: 
        print('You must enter', number_dice, 'choices') 
        user_choices = input("For each die, type - to hold or r to roll again: ") 

    #roll again based on user choices 
    roll_again(user_choices, user_rolls) 
    print("Player's new roll: ", user_rolls)

    computer_choices = computer_advanced(number_dice)
    roll_again(computer_choices, computer_rolls)
    print("Computer's new roll: ", computer_rolls)
    reroll_count += 1
    if reroll_count < 3:
        reroll = input("Do you want to reroll any of your dice? y or n: ")
    else:
        reroll = "n"

computer_total = sum(computer_rolls) 
user_total = sum(user_rolls) 
print("Computer's total: ", computer_total) 
print("User's total: ",user_total ) 
print(find_winner(computer_rolls, user_rolls))

