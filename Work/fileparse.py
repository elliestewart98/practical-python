# fileparse.py
#
# Exercise 3.3
import csv

#Read a csv file into a list of dictionaries
def parse_csv_1(filename):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        records = []
        for row in rows:
            if not row:
                continue #skips row with no data
            record = dict(zip(headers,row))
            records.append(record)
    return records

portfolio = parse_csv_1('Data/portfolio.csv')
print(portfolio)


#Now allow you to optionally specify the columns 
def parse_csv_2(filename, select = None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
            
        records = []
        for row in rows:
            if not row:
                continue #skips row with no data
            if indices:
                row = [row[index] for index in indices]
                
            record = dict(zip(headers,row))
            records.append(record)
    return records

shares_held = parse_csv_2('Data/portfolio.csv', select=['name','shares'])
print('\n',shares_held)

# Modify the parse_csv() function so that it 
# optionally allows type-conversions to be applied
# to the returned data.

def parse_csv_3(filename, types = None, select = None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
            
        records = []
        for row in rows:
            if not row:
                continue #skips row with no data
            if indices:
                
                row = [row[index] for index in indices]
                if types:
                    row = [func(val) for func,val in zip(types,row)]
                    
        
            record = dict(zip(headers,row))
            records.append(record)
    return records

shares_held = parse_csv_3('Data/portfolio.csv', 
                        select=['name', 'shares'],
                        types=[str, int])
#print(shares_held)
"""
# Modify the parse_csv() function so that it can work 
# with such files by creating a list of tuples instead. 
def parse_csv_4(filename, types = None, select = None, has_headers = True):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        
        # Read the file headers (if any)
        headers = next(rows) if has_headers else []
        
        if has_headers:
            headers = next(rows)
            
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []
                
            records = []
            for row in rows:
                if not row:
                    continue #skips row with no data
                if indices:
                    
                    row = [row[index] for index in indices]
                    if types:
                        row = [func(val) for func,val in zip(types,row)]
                        
            
                record = dict(zip(headers,row))
                records.append(record)
        else:
            records = []
            for row in rows:
                if not row:
                    continue #skips row with no data
                if types:
                    row = [func(val) for func,val in zip(types,row)]
                    
                record = (item for item in rows)
                records.append(record)
    return records
"""

def parse_csv_4(filename, select=None, types=None, has_headers=True, delimiter=','):
    '''
    Parse a CSV file into a list of records with type conversion.
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers (if any)
        headers = next(rows) if has_headers else []

        # If specific columns have been selected, make indices for filtering 
        if select:
            indices = [ headers.index(colname) for colname in select ]
            headers = select

        records = []
        for row in rows:
            if not row:     # Skip rows with no data
                continue

            # If specific column indices are selected, pick them out
            if select:
                row = [ row[index] for index in indices]

            # Apply type conversion to the row
            if types:
                row = [func(val) for func, val in zip(types, row)]

            # Make a dictionary or a tuple
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

        return records


prices = parse_csv_4('Data/prices.csv', types=[str,float],
                   has_headers=False)

print('\n', prices)


# Modify the code so that an exception gets raised if both 
# the select and has headers arguments are passed

def parse_csv_5(filename, select=None, types=None, has_headers=True, delimiter=','):
    '''
    Parse a CSV file into a list of records with type conversion.
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        if select and (has_headers == False):
            raise RuntimeError('Cannot select headers if there are none.')
        
        # Read the file headers (if any)
        headers = next(rows) if has_headers else []

        # If specific columns have been selected, make indices for filtering 
        if select:
            indices = [ headers.index(colname) for colname in select ]
            headers = select

        records = []
        for row in rows:
            if not row:     # Skip rows with no data
                continue

            # If specific column indices are selected, pick them out
            if select:
                row = [ row[index] for index in indices]

            # Apply type conversion to the row
            if types:
                row = [func(val) for func, val in zip(types, row)]

            # Make a dictionary or a tuple
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

        return records
"""
prices_fail = parse_csv_5('Data/prices.csv',
                        select=['name','price'],
                        has_headers=False)
"""
# Modify the function to catch all ValueError exceptions
# generated during record creation and print a warning
# message for rows that cant be converted. 

def parse_csv_6(filename, select=None, types=None, has_headers=True, delimiter=','):
    '''
    Parse a CSV file into a list of records with type conversion.
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        if select and (has_headers == False):
            raise RuntimeError('Cannot select headers if there are none.')
        
        # Read the file headers (if any)
        headers = next(rows) if has_headers else []

        # If specific columns have been selected, make indices for filtering 
        if select:
            indices = [ headers.index(colname) for colname in select ]
            headers = select

        records = []
        row_number = 0
        for row in rows:
            if not row:     # Skip rows with no data
                continue

            # If specific column indices are selected, pick them out
            if select:
                row = [ row[index] for index in indices]
                row_number +=1

            # Apply type conversion to the row
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                    row_number +=1
                except ValueError as e:
                    print
                    print('Row',row_number,': Couldnt convert ', row )
                    print(e)
            # Make a dictionary or a tuple
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

        return records

print('\n ------- \n ValueError check: \n ')
portfolio = parse_csv_6('Data/missing.csv', types=[str, int, float])








