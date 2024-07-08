#Introduction
print('Hello, my name is Ada. I am a chatbot!')
print('I like animals and I love to talk about food')
name = input('What is your name?: ')
print('Hello ' + name + ', Nice to meet you')

# get year information
year = input('What is the current year?: ')
print("Yes, that's right. Thanks! ")
# ask user to guess age
age = input('Can you guess my age? Please enter a number: ')
print('You got it! I am ' + age + ' years old')
# do math to calculate when chatbot will be 100
age = int(age)
numYears = 100 - age
print('I will be 100 in ' + str(numYears) + ' years')
print('That will be the year ' + str(int(year) + numYears))

# food conversation
print('I love burgers and I also like trying out new kinds of food')
food = input('How about you? What is your favorite food?: ')
print("Huh, I've never tried " + food + '!')
q = 'Where do you get ' + food + '?: '
location = input(q)
print("Interesting. I'll have to try it out")

# animal conversation
animal = input('My favorite animal is a platypus. What is yours?: ')
print(animal + '! I am scared of them.')
print('I wonder if a ' + animal + ' likes to eat ' + food + '?')

#conversation about feelings
mood = input('How are you feeling today?: ')
print('Why do you think you are feeling ' + mood + '?')
reason = input("Please tell me: ")
print('Thank you for sharing!')

#goodbye
print('...beep...beep...losing power')
print('Goodbye, ' + name + '. It was fun to talk with you today!')
