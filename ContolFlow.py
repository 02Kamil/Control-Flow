# Date: 2-3-20
# Programmer: Kamil Allishaw

name = input("\nwhat is your name?: ")
x = 15


# Greeting Function
def greeting():
    print("Hello there " + name)
    print("Nice to meetcha!")
    print(x)


# Functions and & Local Variables
def printSomething():
    x = 3
    print(x)


# Functions and Parameters
def PrintN(age):
    print(age)


# Default Parameter values
def Print2N(x,y = 69):
    print("First parameter #: " + str(x))
    print("Second Parameter #: " + str(y))

# Print Sum
def PrintSum(x,y):
    print(x + y)

# Print Multiple TImes
def PrintMulti(string, times):
    for i in range(times):
        print(string)

print("\n****Greetings Function****\n")
greeting()
print("\n****Print Something Function****\n")
printSomething()
print(x)
print("\n****Print Number Function****\n")
PrintN(18)
PrintN(69)
print("\n****Print 2 number Function****\n")
Print2N(7,3)
Print2N(32)
print("\n****Print Sum Function****\n")
PrintSum(4,9)
print("\n****Multi Print Function****\n")
PrintMulti("ILCS",3)
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



#Programmer: Kamil Allishaw
#Date: 12/19/19
#Program: One through Ten


x = 1

#While Loop will see if a condition has been met

while x <= 10:
    print(x)
    x+=1

# Programmer: Kamil Allishaw
# Date: 1/6/20
# Program: Running Total. PART II

#This program asks the user for 5 numbers and then sums them

z = 0
r = int(input("\nHow many numbers would you like to add together?: "))

for j in range(r):
    d = int(input("\nEnter a number: "))
    z = z + d

print("\nYou sum is: " + str(z))

print("Use a calculator next time maybe?")


#Programmer: Kamil Allishaw
#Date: 1/6/20
#Program: Average Test Scores


T = 0

n = int(input("\nHow many tests do you wish to average?: "))

for i in range(n):
    s = float(input("\nTest score: "))
    T = T + s

a = T / n

print("\nThe Average across the scores is: " + str(round(a, 3)))



# Programmer: Kamil Allishaw
# Date: 1-20-20
# Program Double for loop

for i in range(3):
    print("\nHi! I'm outside " + str(i))
    for j in range(2):
        print("\n\tHi! I'm inside " + str(j))

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
