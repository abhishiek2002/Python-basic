# _________________ Functions _________________

# function is a block of code, that perform a specific task.

# fuctions can be called any time in the code

# That's why it is called reusable code.



# Types Of functions :-- 



# 1. In-built(pre-defined)(built-in) functions
# eg:- print(), insert(), input(), int()



# 2. User defined functions 
#  user defined functions defined by user itself


# syntax to define function :-

#       def function_name(parameters){
#           function code...
#       }


#  calling a function :-

#            function_name()


# function of add two numbers

# function defining
def add_two(num1,num2):
    output = num1 + num2
    return output  # it exit the function and return the output.

# function calling

a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))
        
# output = add_two(num1 = a, num2 = b)   # assign value to parameters

#  postional arguments :- because we have not declared where a & b goes . So, interpreter take according to their position
output = add_two(a,b)


print("addition of two numbers {a} & {b} is : ",add_two(a,b))



marks = [41,52,63,36,25,14,47,58,69,96,85,74]

print(len(marks))


# creating my_len function which return same value as "len()" function

def my_len(ls) :
    count =0
    for item in ls :
        count+=1
    
    return count


print(my_len(marks))

# defining a function that add all item of list

def add_items(ls) :
    count =0
    for item in ls :
        count+=item
    return count

print(add_items(marks))


# avaerage_finder

def add_items(ls) :
    count =0
    total =0
    for item in ls :
        count+=1
        total+=item
    return total/count



# even_finder
# average_even_finder

