# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 17:36:41 2025

@author: rafae
"""

##
#This Program will convert a value of inches to centimeters. We will conver to 2 decimal places to 
# although sixty-fourths goes into 6 decimal places for inches we will output Centimeters

#Printing out the prompt for the user with a centipede
print("Convert Inches into Centimeters!🐛")
print("Note: Inches may use up to 6 decimals to express the fraction, but it will out put centimeters in two decimal places.")

#Taking in the input of inches to convert
varInches = float(input("Please enter the inches you would like to convert: "))

#Using arithmetic formula to convert inches into centimeters with 2 decimal places rounded
converterThreeThousand = round(varInches * 2.54, 2)

#output of the conversion to the user
print("The conversion is",converterThreeThousand, "cms")