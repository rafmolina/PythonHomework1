# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 16:17:16 2025

@author: rafael
"""
## 
#This is a program that takes in 5 numbers (float, using 8 bytes) without creating functions. These five numbers are then output with sum, product, and average as
# well as outputting the input numbers from the user. It will be user friendly containing strings for both input and output prompts. All withing Chapter 1-2 Python 4 Every1
#

#introduction to the user, user is able to put in numbers past 2 decimal points
print("Welcome to the 5 number arithmetic program")
print("Prepare to enter 5 numbers below, decimal numbers may be entered")

#creating Variables for the program, all five inputs
varOne = float(input("Please enter the first number: "))
varTwo = float(input("Please enter the second number: "))
varThree = float(input("Please enter the third number: "))
varFour = float(input("Please enter the fourth number: "))
varFive = float(input("Please enter the fifth number: "))

#Arithmetic for the input numbers. 
sumOfFive = varOne + varTwo + varThree + varFour + varFive
productOfFive = varOne * varTwo * varThree * varFour* varFive
averageOfFive = (varOne + varTwo + varThree + varFour + varFive) / 5

#printing out whats requested, with a round of 2 decimal points 
print("The numbers you have entered are: ", varOne, varTwo, varThree, varFour, varFive)
print("The sum of the numbers you have entered is: ", round(sumOfFive,2))
print("These numbers multiply to equal: ",  round(productOfFive,2))
print("Lastly, the average of the 5 numbers is: ", round(averageOfFive,2))