#Write a program using functions to Compute the monthly payment, given the loan amount, number of years and
#the annual interest rate.


loan_amt = float(input("enter loan amount: "))
num_of_years = int(input("enter no of years: "))*12



def emi (loan_amt,num_of_years):

    
    annual_interest_rate = 7

    interest_rate = (loan_amt * annual_interest_rate)/100
    print(f"total interest {interest_rate}")

    total_loan_amount = (loan_amt + interest_rate)//num_of_years
    print(f"monthly amount user have to pay: {total_loan_amount} ")

emi(loan_amt,num_of_years)









