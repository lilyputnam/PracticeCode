#quiz.py
#This program would be used to create a quiz with definite answers.

print("Welcome to the quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Let's play :)")
score = 0

answer = input("What colour is the sky? ")
if answer.lower() == "blue":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#learning how to increment number to keep score

answer = input("What is the capital of New Zealand? ")
if answer.lower() == "wellington":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#using .lower() is good to use in case they type the answer correctly but in capitals

answer = input("How many days of the year are there? ")
if answer == "365":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the Prime Minister? ")
if answer.lower() == "jacinda ardern":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4)*100) + "%")

#calculating a percentage



