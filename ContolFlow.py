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

