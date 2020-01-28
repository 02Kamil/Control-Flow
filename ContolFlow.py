
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