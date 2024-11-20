# Question and Answer game

print("You will get 2 marks for correct answer and\n0.5 negative marks for incorrect answer.")
while True:
    print("----------------------------")
    answer = input("Do you want to play? (y/n) \n").lower()
    if answer == "n":
        quit()
    elif answer != "y":
        print("Please write (y/n)")
    else:
        break

print("Ok Let's Play")

score = 0
correct = 0
incorrect = 0

# Question 1
print("1) What is the capital city of Canada?")
answer = input(
    "(a) Toronto b) Vancouver c) Ottawa d) Montreal) \nAnswer: ").lower()

if answer == "ottawa" or answer == "c":
    print("Correct!")
    score += 2
    correct += 1
else:
    print("Incorrect")
    score -= 0.5
    incorrect += 1


# Question 2
print("2) What is the chemical symbol for gold?")
answer = input("a) Au  b) Ag  c) Pb  d) Fe \nAnswer: ").lower()
if answer == "au" or answer == "a":
    print("Correct!")
    score += 2
    correct += 1
else:
    print("Incorrect!")
    score -= 0.5
    incorrect += 1


# Question 3
print("3) Who was the first president of the United States?")
answer = input(
    "a) Thomas Jefferson b) Benjamin Franklin c) George Washington d) Abraham Lincoln \nAnswer: ").lower()
if answer == "george washington" or answer == "c":
    print("Correct!")
    score += 2
    correct += 1
else:
    print("Incorrect!")
    score -= 0.5
    incorrect += 1


# Question 4
print("4) How many days are there in a leap year?")
answer = input(
    "a) 365  b) 366  c) 364  d) 367 \nAnswer: ").lower()
if answer == "366" or answer == "b":
    print("Correct!")
    score += 2
    correct += 1
else:
    print("Incorrect!")
    score -= 0.5
    incorrect += 1


print("--------------------------")
print("You answer", correct, "correct answers.")
print("You answer", incorrect, "incorrect answers.")
print("After negative marking.")
print("Your final score is ", score)
