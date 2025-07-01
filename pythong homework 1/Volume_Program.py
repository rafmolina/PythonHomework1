# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 17:06:12 2025

@author: rafael
"""

##
#This program is built to find the volume of a rectangle prism. It will ask the user to input
#the length, width, and height of the rectangle in order to output the volume. The numbers
# will all be in 2 demical value and be user friednly.
#

#Introduction to the program for attaining the volume of a space
print("Hello and welcome to the volume program 5000")
print("In order to produce the volume, you will enter the length, width, and height of your space")
print("This program is meant for measurements in feet, please enter decimals for partial feet")
print("Note: decimals will be rounded into 2 decimal places")

#Creating Variables for the inputs
varOne = float(input("Please enter the length of the space: "))
varTwo = float(input("Please enter the width of the space: "))
varThree = float(input("Please enter the height of the space: "))

#Rounding the Variables, all units myst be withing 2 decimals
roundedVarOne = round(varOne, 2)
roundedVarTwo = round(varTwo, 2)
roundedVarThree = round(varThree, 2)

#Arithmetic formula for attaining the Volume
volumeOfSpace = roundedVarOne * roundedVarTwo * roundedVarThree
#Overkill rounding for better practice 
roundedVolumeOfSpace = round(volumeOfSpace)

print("The volume of your space is:",roundedVolumeOfSpace,"ft")
