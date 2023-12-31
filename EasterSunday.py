# File: EasterSunday.py
# Student: Alec Anaya
# ET EID: AA89468
# Course Name: CS303E
#
# Date: 2/5/2022
# Description of program: The purpose of this program is to obtain an input, a year,
# from a user and have coded an algorithm that tells them the month and day Easter sunday falls on. 
print()
y = int(input('Enter year :'))
# Code for the algorithm of obtaining desired date
a = y % 19
b = y // 100
c = y % 100
d = b // 4
e = b % 4
g = (8 * b + 13) // 25
h = (19 * a + b - d  - g + 15) % 30
j = c // 4
k = c % 4
m = (a + 11 * h) // 319
r = (2 * e + 2 * j - k - h + m + 32) % 7
n = (h - m + r + 90) // 25
p = ( h - m + r + n + 19) % 32
# Printing of sloution
print('In', y ,'Easter Sunday is on month', n ,'and day', p )
print()

