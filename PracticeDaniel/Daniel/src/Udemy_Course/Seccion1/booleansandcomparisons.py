# # Booleans / True / False
# truthy = True
# falsy = False
# age = 20
# is_over_age = age>= 18 # greather than
# #the result for is_over_age and age 20 is True
# print(is_over_age)
# is_under_age = age<= 18 # less than
# is_twenty = age == 20 #equal than
#
# #and & or python
#
# print(bool(34)) #print True
# print(bool("Hello")) #print True
# print(bool(0)) #print False
# print(bool(""))#print False

#and gives you the first value if it is False,otherwise it gives you the second value

x = True and False
print(f'Test and with True and False, value of x: ', x)
x = False and True
print(f'Test and with False and True, value of x: ', x)
x = 35 and 0
print(x)

#or gives you the first value if it is True, otherwise it gives you the second value

x = True or False
print(f'Test or with True or False, value of x: ', x)
x = False or True
print(f'Test or with False or True, value of x: ', x)
x = False or False
print(f'Test or with False or False, value of x: ', x)
x = True or True
print(f'Test or with False or False, value of x: ', x)

x = 35 or 0
print(x)

#operator not in fron of boolean, does the opposite of the boolean
print(not True) #print False
print(not False) #print True
print(not 35) #print False, because bool(35) is True

cmp = 15 > 20 or 17 < 20
print(cmp)

