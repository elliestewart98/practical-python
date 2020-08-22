# pcost.py
#
# Exercise 1.27
# Write a program called pcost.py that opens this file,
# reads all lines, and calculates how much it cost to 
# purchase all of the shares in the portfolio.
# Should print out: Total cost 44671.15
import csv
"""
def portfolio_cost(filename):  
    with open(filename, 'rt') as f:
        #this reads in the first line and means you can skip the column headers
        headers = next(f)
        name = []
        shares = []
        prices = []
        print(f)
        rows = csv.reader(f, delimiter = ',')
        for column in rows:
            name.append(column[0])
            shares.append(float(column[1]))
            prices.append(float(column[2]))
            print(column)
    
        
        share_prices = []
        for i in range(len(shares)):
            share_prices.append(shares[i]*prices[i])
        return(sum(share_prices))
"""       
#Given solution
def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost


cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
