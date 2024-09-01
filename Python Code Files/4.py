# <<<<<<<<<<<<<<<<<<<<<<<<<<<<< DICTIONARY >>>>>>>>>>>>>>>>>>>>>>
    # IT IS DIFFERENT FROM SET IN ONLY ONE MANNER THAT IT HAS VARIABLE AND IT'S VALUE SO THAT WE CAN DIFFERENTIATE VALUES AND VARIABLES


# eg:- we need construct a set a student with their numbers of maths subject then we can't substitute value of maths marks in set that's why we use dictionary

# dict = {key:value}   duplicate key is not allowed

d = { 'mohit':23, 'Abhishek kuntal':65, 'Aditya':56,  65:'abhishek' , 'mohit':34}
print(d['Abhishek kuntal'])   #var[key] to excess value of key
print(d[65])
print(type(d))
print(d['mohit'])  #if two key are similar then it can last value

d['Abhishek kuntal']=75  #update value of any particular key
print(d)

d['Abhishek kuntal','Aditya','mohit']=79,63,56  #it take('Abhishek kuntal','Aditya','mohit') as a single entity
print(d)  


d['rahul']=35  #if we are updating any value of key and key is not exist in dictionary then it will behave as inserting 

print(d.keys())  #to print all keys of dictionary only

print(d.values())  #to print all values of dictionary only

# remove any key value pair from dictionary

d.pop('rahul')
print(d)

d.pop('Aditya', 'mohit')
print(d)

#   create a dictionary which have 5 student names,marks,subject

students = {'Name':['abhishek','rohit','mohit','ritu','yash','jugnu'], 'Marks':[79,52,14,36,45,96], 'Subject':'Science'}

print(students)
print(type(students))
print(students['Name'])
print(students['Marks'])
print(students['Subject'])


science_marks = {'Name':['abhishek','rohit','mohit','ritu','yash','jugnu'], 'Marks':[79,52,14,36,45,96], 'Subject':'Science'}

# we have to remove "ritu" and her marks

science_marks['Name'].remove('ritu')  #science_marks['Name'] is a list so we can perform any list operation on that
science_marks['Marks'].remove(36)
print(science_marks)

# lets update marks of mohit by 41

science_marks['Marks'][2]=41
print(science_marks)






# <<<<<<<<<<<<<<<< TYPE CASTING >>>>>>>>>>>>>>>>>>

# int(), float(), str(), list(), tuple(), list(), set(), dict() 

num1=10

num1=float(num1)  #int convert into float
print(num1)  #10.0
print(type(num1))



num2=20.25

num2=int(num2) #float convert into int
print(num2)  #20
print(type(num2))


ls=[10,1,0,10,80,90,80,80,45,90]

# let remove duplicate values in "ls" list with help of type casting

ls = set(ls)  #set remove all duplicate value
ls = list(ls)
print(ls)
print(type(ls))



# <<<<<<<<<<<<<<<<<< Operators >>>>>>>>>>>>>>>>>


# 1. Arithmatic Operators

num1 =int(input("Plz Enter Num 1 : ")) #input always takes value as a string that's why typecast input into your desire datatype
num2 =int(input("Plz Enter Num 2 : "))

# add "+"

output = num1+num2
print(output)

#subtract "-"
output = num1-num2
print(output)

#multiply "*"
output = num1*num2
print(output)

#divide "/"
output = num1/num2  #it is different from other language like c++,java because "/" give  int,float value depend on type of operand and in python "/" give only float value. So, if you want only int value then type cast it into int.
# output = int(num1/num2)
print(output)

# module "%" give reminder
output = num1%num2
print(output)


# "**" it is power operator

output = num1**num2;
print(output)


# "//" floor division operator (it gives quotients of a/b )

output = num1//num2;
print(output)
