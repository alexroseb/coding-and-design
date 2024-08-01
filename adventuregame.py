import time
import sys
print("""
 ██████   ██████                                ███                     
░░██████ ██████                                ░░░                      
 ░███░█████░███   ██████  ████████  ████████   ████  ████████    ███████
 ░███░░███ ░███  ███░░███░░███░░███░░███░░███ ░░███ ░░███░░███  ███░░███
 ░███ ░░░  ░███ ░███ ░███ ░███ ░░░  ░███ ░███  ░███  ░███ ░███ ░███ ░███
 ░███      ░███ ░███ ░███ ░███      ░███ ░███  ░███  ░███ ░███ ░███ ░███
 █████     █████░░██████  █████     ████ █████ █████ ████ █████░░███████
░░░░░     ░░░░░  ░░░░░░  ░░░░░     ░░░░ ░░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░███
                                                                ███ ░███
 ███████████                        █████     ███              ░░██████ 
░░███░░░░░███                      ░░███     ░░░                ░░░░░░  
 ░███    ░███   ██████  █████ ████ ███████   ████  ████████    ██████   
 ░██████████   ███░░███░░███ ░███ ░░░███░   ░░███ ░░███░░███  ███░░███  
 ░███░░░░░███ ░███ ░███ ░███ ░███   ░███     ░███  ░███ ░███ ░███████   
 ░███    ░███ ░███ ░███ ░███ ░███   ░███ ███ ░███  ░███ ░███ ░███░░░    
 █████   █████░░██████  ░░████████  ░░█████  █████ ████ █████░░██████   
░░░░░   ░░░░░  ░░░░░░    ░░░░░░░░    ░░░░░  ░░░░░ ░░░░ ░░░░░  ░░░░░░    
""")
inventory = []
print("Good morning! Can you make it out of the house?")
print("It seems easy, however you may encounter some interesting obstacles.")
print("Let's start. You get out of bed and open your bedroom door. Outside, you see...")
time.sleep(2)
print("A grizzly bear!")
time.sleep(0.5)
choice1 = input("""What do you do?
a: Go back inside your bedroom
b: Yell at the bear
c: Ignore the bear
Choice: """)
while not (choice1.lower() == "a" or choice1.lower() == "b" or choice1.lower() == "c"):
    choice1 = input("Sorry, did you mean a, b, or c? ")
if choice1.lower() == "a":
    print("An understandable response to seeing a bear inside your house.")
    print("However, now you are trapped. Let's make use of this time to pick up an item.")
    choice2 = input("Would you rather have your keys or your phone? ")
    while not (choice2.lower() == "keys" or choice2.lower() == "phone"):
        choice2 = input("Type 'keys' or 'phone': ")
    if choice2.lower() == "keys":
        inventory.append("keys")
        print("Now armed with your keys, you reopen the door. Shaking the keys startles the bear and it runs away.")
    elif choice2.lower() == "phone":
        inventory.append("phone")
        print("You use your phone to call Animal Control, who come and get the bear out of your house.")
elif choice1.lower() == "b":
    print("Brave choice! The bear is startled and runs away.")
    print("You have recieved the Bravery Badge. This may be useful later.")
    inventory.append("bravery_badge")
elif choice1.lower() == "c":
    print("You decide that you haven't had your coffee yet so you must be imagining the bear.")
    print("Unfortunately, it is indeed there. The bear growls and rushes you....")
    time.sleep(1)
    print("GAME OVER. You were eaten by the bear.")
    sys.exit(0)
print("Bear dealt with, it's time to keep going with your morning. You go brush your teeth and wash your face.")
print("Your cupboards are pretty empty. What would you like to eat for breakfast?")
c3in = """a: potentially sketchy leftovers
b: dry cereal"""
if "phone" in inventory:
    c3in += """
c: Call out for delivery
Choice:"""
else:
    c3in += """
Choice:"""
choice3 = input(c3in)
while not (choice3.lower() == "a" or choice3.lower() == "b" or choice3.lower() == "c"):
    choice3 = input("Sorry, did you mean a, b, or c? ")
if choice3.lower() == "a":
    print("Really?? That's your choice??")
    time.sleep(1)
    print("GAME OVER. You got food poisoning.")
    sys.exit(0)
elif choice3.lower() == "b":
    print("Uninspiring, but filling.")
else:
    print("You're lucky you have your phone with you! You eat a delicious pancake breakfast.")
choice4 = input("""Last choice: do you want to drive or walk to work?
Choice: """)
while not (choice4.lower() == "drive" or choice4.lower() == "walk"):
    choice4 = input("Type 'drive' or 'walk': ")
if choice4.lower() == "drive":
    if "bravery_badge" in inventory:
        print("While driving to work, you are confronted with an overwhelming sense of fear. Luckily you have a bravery badge to help you out!")
        print("GAME OVER. You made it to work successfully!")
    else:
        print("While driving to work, you are confronted with an overwhelming sense of fear. Too bad you don't have a bravery badge to help you through...")
        time.sleep(1)
        print("GAME OVER. You succumbed to existential dread.")
else:
    print("Your walk to work is almost strangely uneventful. Looks like you're going to have a good day!")
    print("GAME OVER. You made it to work successfully!")