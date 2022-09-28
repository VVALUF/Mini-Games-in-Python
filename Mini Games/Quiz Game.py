print("Welcome to my quiz!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")
    print("The answer was: central processing unit ")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    print("The answer was: random access memory ")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    print("The answer was: power supply ")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
