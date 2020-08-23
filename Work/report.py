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

#This prints it out clearly with one dictionary on each line
from pprint import pprint
pprint(portfolio)

# Function that reads a set of prices such as prices.csv into
# a dictionary where the keys are stock names and values are stock
# prices. 
"""
def read_prices(filename):
    stock = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        try:
            for row in rows:
                portfolio_dict = {}
                portfolio_dict[row[0]] = row[1]
                stock.append(portfolio_dict)
    return stock
"""
def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices


prices = read_prices('Data/prices.csv')
print(prices['IBM'])
print(prices['MSFT'])

#Compute the current value of the portfolio along with the gain/loss

for stock in portfolio:
    name = stock['name']
    share = stock['shares']
    share_price = stock['price']
    stock_price = prices[name]
    difference = stock_price - share_price
    current_value = share * stock_price
    profit = share * difference
    print("Name: " + name + " Current value: " + str(current_value)
          +" Gain/loss: " + str(profit))

# Write a function make_report() that takes a list of stocks
# and dictionary of prices as input and returns a list of 
# tuples containing the rows of the above table.   
def make_report(portfolio, prices):
    list_of_rows = [] 
    for stock in portfolio:
        name = stock['name']
        share = stock['shares']
        initial_price = stock['price']
        current_price = prices[name]
        difference = current_price - initial_price
        current_value = share * current_price
        profit = share * difference
        holding = (name,share, current_price, difference)
        list_of_rows.append(holding)
        print("Name: " + name + " Current value: " + str(current_value)
              +" Gain/loss: " + str(profit))
    return list_of_rows

report = make_report(portfolio,prices)
# This formats the report as a table by formatting the tuples
"""
for r in report:
    print('%10s %10d %10.2f %20.2f' % r)
"""   
# Or you can expand the values and use fstrings
# This aligns them all evenly by decimal point
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')



