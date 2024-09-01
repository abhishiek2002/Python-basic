name = input("Plz enter your name : ")
print("Hello ",name)

balance = 1000

message = """
How may I help you sir?

Please select any one of the option :-
Type 1 >>>> check balance
Type 2 >>>> Deposit
Type 3 >>>> Withdraw

"""
print(message)
op = int(input("Enter option : "))

if op in {1,2,3} :           # "pass keyword is used when we don't want to write code for now but we will write code after "
    print("Welcome to you in virtual bank program")
    if op ==1 :
        print("Your available balance is : " , balance)
    elif op ==2 :
        deposit_balance = int(input("Enter your deposit amount : "))
        if deposit_balance>0 :
            balance+= deposit_balance
            print("Your available balance is : " , balance)
        else :
            print("Enter valid amount")    
    else :
        withdraw_amt = int(input("Enter amount to withdraw : "))
        if (withdraw_amt<=balance) :
            balance-=withdraw_amt
            print("Now your available balance is : " , balance)
        else :  
            print("Either your withdraw amount is greater  than available balance or invalid withdraw amount ")  
            



else :
    print("Plz choose valid option")    

