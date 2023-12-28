print("Welcome to my biology quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay let's play and have fun!")
score = 0

answer = input("What does DNA stand for? ")
if answer.lower() == "deoxyribonucleic acid":
    print("Correct, great job!")
    score += 1
else:
    print("Sorry you are wrong")

answer = input("What is the process in which plants make their own food? ")
if answer.lower() == "photosynthesis":
    print("Correct, great job!")
    score += 1
else:
    print("Sorry you are wrong")

answer = input("What is the smallest unit of life? ")
if answer.lower() == "cell":
    print("Correct, great job!")
    score += 1
else:
    print("Sorry you are wrong")

answer = input("What is the structure that connects the muscles to the bones? ")
if answer.lower() == "tendon":
    print("Correct, great job!")
    score += 1
else:
    print("Sorry you are wrong")

answer = input("What is the body's first line of defense against infections? ")
if answer.lower() == "skin":
    print("Correct, great job!")
    score += 1
else:
    print("Sorry you are wrong")

print("You got " + str(score) + " questions correct!")
print("Thank you for playing")
    