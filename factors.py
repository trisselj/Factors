# Author: Jake Trissel
# Github Username: trisselj
# Date: 07/10/2024
# Description: Prints out the factors of an integer entered

#Initial integer request
Integer = int(input("Please enter a positive integer: "))

#In case someone enters a negative integer and initial printed response
if Integer <=0:
    print("Please print a positive integer, thanks.")
else:
    print(f"The factors of {Integer} are:")

#Starts with 1 and adds 1 dividing by the numeber each time and checking if there is a remainder before printing if remainder = 0
for i in range(1, Integer + 1):
    if Integer % i == 0:
        print (i)