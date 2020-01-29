

#Programmer: Kamil Allishaw
#Date: 12/16/19
#Program: Guess my Number

MyNumber = 4

print("\nGuess a number between One & Ten.\n")

#ASk users to guess

guess = int(input("Enter a Guess : "))

#Keep asking users to guess number until correct

while guess != MyNumber:
    if guess == 69:
        print("\nNice. Try again though.")
    else:
        print("\nNot Quite. Try Again!")
    guess = int(input("\nEnter another Guess : "))

print("\nCorrect! Good job.\n")


# Programmer: Kamil Allishaw
# Date: 1-20-20
# Program Double for loop

for i in range(3):
    print("\nHi! I'm outside " + str(i))
    for j in range(2):
        print("\n\tHi! I'm inside " + str(j))

# Programmer: Kamil Allishaw
# Date: 12/19/19
# Program: One through Ten


x = 1

#While Loop will see if a condition has been met

while x <= 10:
    print(x)
    x+=1

# Programmer: Kamil Allishaw
# Date: 1/6/20
# Program: Running Total. PART II

# This program asks the user for 5 numbers and then sums them

z = 0
r = int(input("\nHow many numbers would you like to add together?: "))

for j in range(r):
    d = int(input("\nEnter a number: "))
    z = z + d

print("\nYou sum is: " + str(z))

print("Use a calculator next time maybe?")


# Programmer: Kamil Allishaw
# Date: 1/6/20
# Program: Average Test Scores


T = 0

n = int(input("\nHow many tests do you wish to average?: "))

for i in range(n):
    s = float(input("\nTest score: "))
    T = T + s

a = T / n

print("\nThe Average across the scores is: " + str(round(a, 3)))

"""
Programmer: Kamil A
Date: 1-23-20
Program: WHile inside a for
"""

for i in range(4):
    print("for Loop: " + str(i))
    kool = i
    while kool >= 0:
        print ("\tWhile Loop: " + str(kool))
        kool = kool - 1

