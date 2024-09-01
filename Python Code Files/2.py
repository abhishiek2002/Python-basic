var = 34
# here var is identifier , = is assign operator , 34 is value of identifier





#  rules of naming identifier
# A-Z , a-z , 0-9 only these sign allow in the name of identifiers
# identifier name can't start with number eg (0-9)
mohit = 10
print(mohit)
# identifier names are case sensitive
age = 25
AGE = 20
Age = 15
# all three above variables are different due to case sensitivity. 
print(age , AGE , Age)


age = 12
print(age)

# do not use reserved keywords in naming of variables

# print = 2  #here interpreter does't show error because python convert "print" reserved keyword into variable
# print(print) #but here interpreter show error because python already convert "print" reserved keyword into variable that's why "print" can't use as reserved keyword


_ = 2

print(_)  #  '_' is valid variable name


#  in python datatype define is not necessary

# types of data types

# int 
# flaot
# char

#<<<<<<string>>>>>>>>>>  and  <<<<<<<string methods >>>>>>>>>>

s = "Upflair pvt limited 1233674@#  23.5 0.46"   #double "" and single '' both are valid and same
st = 'Upflair pvt limited 1233674@#  23.5 0.4'

print(s)  # we can write anything in between "" all are valid 
print(st)
print(type(s))

# indexing of characters in a string

# eg U  p  f  l  a  i  r  s  ' '
#    0  1  2  3  4  5  6  7   8  indexing start from 0 to ...
#   -9 -8 -7 -6 -5 -4 -3 -2  -1  indexing in negative  [negative index = positive index - length of string]

st = "Upflairs "

print(st[4])  # it will print 'a'
print(st[2])  #it will print  'f'
print(st[8]) #it will print  ' '


#  2.  find subset of a string

print(st[3:7])  # start from 3 and stop at 6 here 6 include but not 7

# st[starting : stop : jump]   by default jump == 1

print(st[:4]) # start by default is 0
print(st[3:]) # stop by default is "till the end"

print(st[::1]) # jump is 1 by default
print(st[::2]) # jump after every 1 char in string 
print(st[::3]) # jump after every 2 char in string

print(st[::-1]) # fetching string in negative direction output "srialfpU"

st = "Upflairs pvt limited jaipur rajasthan"

# print jaipur
print(st[20:27])
print(st[20-len(st):27-len(st)])

# length of string

print(len(st))

# count iteration of any char or string
print(st.count('j'))
print(st.count('jaipur'))
print(st.count('Jaipur')) #'Jaipur' is not present in string but 'jaiput' is present

# Upper case all string characters

print(st.upper())

# lower case

st2 = st.upper()

print(st2.lower())

print(st.title())
print(st.capitalize())

# replace
print(st.replace('Upflairs','Flipkart'))

print(st.replace('Upflairs','')) # no word to replace so it remove 'Upflairs'

print(st.find('u'))
print(st.endswith('s'))
print(st.startswith('u'))
print(st.split('f')) #The split() method splits the string into substrings if it finds instances of the separator
print(st.strip()) # remove extra space from start and end
# print(st.center())
