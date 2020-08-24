print("Calculator")
lista = ['*', '/', '-', '+']
print("Select your operation")
operation = input(lista)
error = 'Y'

firstnumber = int(input("Enter First Number: "))
secondnumber = int(input("Enter Second Number: "))


while error == 'Y':

    if operation == '*':
        print("Multiplication")
        error = 'N'

    elif operation == '/':
        print("division")
        error = 'N'
    elif operation == '-':
        print('substration')
        error = 'N'
    elif operation == '+':
        print('sum')
        error = 'N'
    else:
        print("please select a valid operation")
        operation = input(lista)



print(firstnumber*secondnumber)






