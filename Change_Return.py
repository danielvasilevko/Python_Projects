#This function is takes in a price and a payment and gives back the remainder or "change" of the transaction
#along with the types of currency that change can be broken down into.

def change_return(cost, given):
    change = round((abs(cost - given)) * 100)
    
    if change == 0:
        print("No change needed.")
        return
    if given < cost:
        print(f"The person paying needs to pay an additional ${cost-given}.")
        return

    owed = change / 100 
    
    dollars = change // 100
    change %= 100  

    quarters = change // 25
    change %= 25  

    dimes = change // 10
    change %= 10

    nickels = change // 5
    change %= 5

    pennies = change

    print(f"The person paying is owed ${owed:.2f}, which can be paid with {dollars} Dollars, {quarters} Quarters, {dimes} Dimes, {nickels} Nickels, and {pennies} Pennies.")

change_return(16.25, 17.89) 
change_return(10, 15.34)
change_return(10.00,10)
change_return(10, 5.67)
change_return(9,10000.89)