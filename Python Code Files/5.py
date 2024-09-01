#  ASSIGNMENT OPERATOR 

                #  It("=") assign value to the variable

x=float(input("Enter number : "))     # assign value 5 in x

                #  "+="

x+=2    # means x=x+2
x+=x+3  # means x=x+(x+3)

                #  "-="

x-=3        # means x = x-3
x-= 3*4     # means x = x-(3*4)

                #  "*="

x*=4        #means x = x*4
x*= x/4     # means x = x*(x/4)

                # "/="

x/=5        # means x = x/5
x/= 3+4*12  # means x = x/(3+4*12)

                #"%="
x%=2        # means x = x%2

                #"//="
x//=5       # means x = x//5


                        #  CAMPARISON OPERATORS


x=int(input("Enter num1 :"))
y=int(input("Enter num2 :"))

#  "=="  EQUAL OPERATOR (TO CHECK VALUE IS SAME OR NOT)

print(x==y)   #give true if x equal to y

#  "!="  NOT EQUALS TO

print(x!=y)   #give true if x is not equal to y

#  "<="  LESS THAN EQUALS TO

print(x!=y)   #give true if x is less than equal to y

#  ">="  GREATER THAN EQUALS TO

print(x!=y)   #give true if x is greater than equal to y



#  <<<<<<<<< IF-ELSE CONDITIONS >>>>>>>>>>>>>>

# SYNTAX :- if (conditions) :
#                code...
#           else:
#               code...

age = int(input("Enter your age : "))

# WRITE A CODE IN WHICH IF AGE IS GREATER THAN 18 THEN PRINT OUT "YOU CAN VOTE AND VICE-VERSA"

if age>18 :
    print("You can vote")

else :
    print("You can not vote")


# <<<<<<<< NESTED IF - ELSE CONDITIONS >>>>>>>>>>>

# WRITE A CODE IN WHICH IF AGE IS GREATER THAN AND LESS THAN 60 THEN PRINT OUT "YOU CAN DRIVE" AND VICE-VERSA

if age>18 :
    if age<60 :
        print("You can drive")
    else :
        print("You can't drive")
else :
    print("You can't drive")


#  <<<<<<<<<<<<<< IF - ELIF - ELSE CONDITIONS >>>>>>>>>>>>>>>

# WRITE A CODE USING IF - ELIF - ELSE CONDITIONS >>>>>>>>>>>>>>>

if age<18 :
    print("you are minor")

elif age>18 and age<60 :
    print("you can drive as well as vote")

else :
    print("you can vote but can't drive")

    

# <<<<<<<<<<<< LOGICAL OPERATORS >>>>>>>>>>>>>>>

# "and" 

print(age>18 and age<60)  # give true if all conditions are true

# "or"  

print(age<18 or age>60)  # give true if atleast one condition is true

# "not"

print(not age>18) 
print(not False)  # give true if condition is false and vice-versa


# WRITE A CODE USING LOGICAL OPERATORS

if age>18 and age<60 :
    print("you can drive")

elif age<18 or age>60 :
    print("you can not drive")

# <<<<<<<<<<<< MEMBERSHIP OPERATORS >>>>>>>>>>>
# <<<<<<<<<<<<<<< "in"  & "not in" operators >>>>>>>>>>>

student_list = ['mohit','ritu','abhishek','manish']

if 'ritu' in student_list :
    print('yes ritu present in list')

if 'ankit' not in student_list :
    print('yes ankit is not present in list')



#  ATM SIMULATION PROGRAM

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





