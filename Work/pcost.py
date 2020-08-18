# pcost.py
#
# Exercise 1.27
# Write a program called pcost.py that opens this file,
# reads all lines, and calculates how much it cost to 
# purchase all of the shares in the portfolio.
# Should print out: Total cost 44671.15
import csv
with open('Data/portfolio.csv', 'rt') as f:
    #this reads in the first line and means you can skip the column headers
    headers = next(f)
    name = []
    shares = []
    prices = []
    print(f)
    readLines = csv.reader(f, delimiter = ',')
    for line in readLines:
        name.append(line[0])
        shares.append(float(line[1]))
        prices.append(float(line[2]))

    
    share_prices = []
    for i in range(len(shares)):
        share_prices.append(shares[i]*prices[i])
    print('\nTotal Cost', sum(share_prices))
        


