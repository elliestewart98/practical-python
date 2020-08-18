# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
N_months = 0


while principal > 0:
    
    if (principal * (1+rate/12)) < payment:
        principal = 0
        total_paid = total_paid + (payment - principal * (1+rate/12))
        N_months +=1
    else:
        if N_months < 12:
            principal = principal * (1+rate/12) - payment - 1000
            total_paid = total_paid + payment + 1000
            N_months +=1
        else:
            principal = principal * (1+rate/12) - payment
            total_paid = total_paid + payment
            N_months +=1
    
    print(N_months, round(total_paid,7), round(principal,7))

print('Total paid', round(total_paid,7))
print('Months' , N_months)