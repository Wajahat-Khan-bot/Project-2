# Question and Answer game


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

# Question 1
print("What is the capital city of Canada?")
answer = input(
    "(a) Toronto b) Vancouver c) Ottawa d) Montreal) \nAnswer:").lower

if answer == "ottawa" or "c":
    print("Correct!")
    score += 2
else:
    print("Incorrect")
    score -= 0.5


# Question 2
print("What is the chemical symbol for gold?")
answer = input("a) Au  b) Ag  c) Pb  d) Fe \nAnswer:").lower()
if answer == "Au" or "a":
    print("Correct!")
    score += 2

else:
    print("Incorrect!")
    score -= 0.5

# Question 3
print("Who was the first president of the United States?")
answer = input(
    "a) Thomas Jefferson b) Benjamin Franklin c) George Washington d) Abraham Lincoln \nAnswer:").lower()
if answer == "c) George Washington" or "c":
    print("Correct!")
    score += 2

else:
    print("Incorrect!")
    score -= 0.5

print(score)
