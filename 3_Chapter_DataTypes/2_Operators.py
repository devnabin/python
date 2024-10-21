'''
There are 4 types of operators in Pyton
1. Arithmetic Operator : +, -, *, / etc
2. Assignment Operator : =, -=, += etc
3. Comparision Operator : ==, >, >=, <, != etc (retrun boolean value)
4. Logical Operator : and, or, not
'''

# 1. Arithmetic Operator : +, -, *, / etc
a = 2-1

# 2. Assignment Operator : =, -=, += etc
a  = 1; # Assign value to a variable
a -= 1; # Decrement a by 1 and then assign to variable a
a += 5; # Increment value of a by 5 and again assign the resultant value to variable a
print(a) # 5

# 3. Comparision Operator : ==, >, >=, <, != etc (retrun boolean value)
b = 5
c = a == b # 5 == 5
print(c) #True

d = 6
c = a == d # 5 == 6
print(c) #False

# 4. Logical Operator : and, or, not
print('\n')
## Logical or Operator
print('-------------- OR --------------')
print ('This is True or False :', True or False)
print ('This is False or True :', False or True)
print ('This is True or True :', True or True)
print ('This is False or False :', False or False)
print('\n')

## Logical And Operator
print('-------------- AND --------------')
print ('This is True and False :',True and False)
print ('This is False and True :',False and True)
print ('This is True and True :',True and True)
print ('This is False and False :',False and False)
print('\n')

## Logical And Operator
print('-------------- NOT --------------')
print('This is not True :', not(True))
print('This is not False :', not(False))

