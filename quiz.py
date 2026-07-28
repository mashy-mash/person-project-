print("Welcome to the Quiz App!")
print("Answer the following questions:\n")

score = 0

# Question 1
print("1. What is the capital of Nigeria?")
print("a) Lagos")
print("b) Abuja")
print("c) Kano")
answer1 = input("Your answer: ").lower()

if answer1 == "b" or answer1 == "abuja":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Abuja.\n")

# Question 2
print("2. What is 15 + 25?")
print("a) 30")
print("b) 40")
print("c) 50")
answer2 = input("Your answer: ").lower()

if answer2 == "b" or answer2 == "40":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is 40.\n")

# Question 3
print("3. Which planet is known as the Red Planet?")
print("a) Earth")
print("b) Mars")
print("c) Jupiter")
answer3 = input("Your answer: ").lower()

if answer3 == "b" or answer3 == "mars":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Mars.\n")

# Final score
print("Quiz finished!")
print("Your score:", score, "out of 3")