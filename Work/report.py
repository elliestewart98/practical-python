# report.py
#
# Exercise 2.4
import csv
"""
#opens a given portfolio file and reads it into a list of tuples
def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio
portfolio = read_portfolio('Data/portfolio.csv')
total = 0.0
for name,shares,price in portfolio:
    total += shares *price
print(total)
"""

#opens a given portfolio file and reads it into a list of dictionaries
def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            portfolio_dict = {}
            portfolio_dict[headers[0]] = row[0]
            portfolio_dict[headers[1]] = int(row[1])
            portfolio_dict[headers[2]] = float(row[2])
            portfolio.append(portfolio_dict)
    return portfolio

portfolio = read_portfolio('Data/portfolio.csv')
print(portfolio)
print(portfolio[1]['shares'])
total = 0.0
for s in portfolio:
    total += s['shares']*s['price']

print(total)

from pprint import pprint
pprint(portfolio)
