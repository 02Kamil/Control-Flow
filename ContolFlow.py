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