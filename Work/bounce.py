# bounce.py
#
# Exercise 1.5

# Write a program that prints a table showing 
# the height of the first 10 bounces.
# Round the output to four digits 
initial_height = 100
height = initial_height
for i in range(9):
	height = height * (3/5)
	print(round(height,4))
