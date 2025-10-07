#Pseudo Code
#get user input monthly sales 
#calc tax per month state, county 
#add state and county 
#display county tax , state tax , total tax
# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month,
# and the amount of state and county sales tax collected.
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.
# Write a program that asks the user to enter the total sales for the month.
# From this figure, the application should calculate and display the following:
# Use at least one function with input and output in this program
#Braden Phetsarath 
#10/7
#Taxes

def state_tax(msales):
    mstatetax = msales * .05
    return mstatetax
def county_tax(msales):
    mcountytax = msales * .025
    return mcountytax
def main():
    msales = float(input("Enter Total Sales for the Month: "))
    mcountytax = county_tax(msales) # The amount of county sales tax.
    mstatetax = state_tax(msales) # The amount of state sales tax.
    print(f"State tax: ${mstatetax:.2f}")
    print(f"County tax: ${mcountytax:.2f}")
    print(f"Total tax: ${(mstatetax + mcountytax):.2f}") # The total sales tax 


if __name__=='__main__':
    main()
