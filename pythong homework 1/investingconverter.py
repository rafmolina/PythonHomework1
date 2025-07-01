# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 18:01:43 2025

@author: rafael
"""

##
# A future value of investment program. The program will ask the user how much money (In US dollars)
# will the user want to invest, for how many years (only years), and the rate of return per year
# the rate of return will be static and the output will be only for the total length of years, NOT THE 
# RETURN OF EVERY YEAR...sorry I started doing that and stopped when I realized I needed functions. 

#Prompt to get ther user to know the program, the program has a bit of personality.
print("Hello there future investor! Investing your money is the smart person's way to grow your wealth")
print("Forget betting, gambling, and buying gold!!!")
print("Instead invest in the banks that keep getting bailed out by the American tax dollars")
print("So please use this investment converter to know how much you can make!")
print("Plese remember we only speak American Dollars $$$$")

#Input variables from the person investing, the US dollar cannot fail 
varInvestingSucker = float(input("So lets start by asking, how much money are you willing to invest? "))
varYearsTricked = float(input("Thats big money! Now how many years would you like us to hold on to that? "))
varBamboozledReturn = float(input("What rate of return did the bank tell you it was? You do not need to enter %, just the number: "))

#Transparent infor for the user, the program is growing with personality...or is it programmer bias?
print("Thanks for the info, we will save it into our database to sell later but give us a sec to let you know how much you'll make!")

#The conversion makes the program think, we divide by 100 to turn that percent into a decimal
convertReturn = varBamboozledReturn / 100
print("......thinking.......")

#Look Ma the American Dream has a formula -- arithmetic for investment values
varReturn = varInvestingSucker * (1+ convertReturn)**varYearsTricked

#Output for the user to know how much money they can now gamble with, true investments
print("You look to make $",round(varReturn,2), "...If the bank survives...")