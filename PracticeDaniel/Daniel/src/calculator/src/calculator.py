print("Calculator")
lista = ['*', '/', '-', '+']

firstnumber = int(input("Enter First Number: "))
secondnumber = int(input("Enter Second Number: "))

print("Select your operation")
operation = input(lista)
error = 'Y'
while error == 'Y':

    if operation == '*':
        print("Multiplication")
        result = firstnumber*secondnumber
        print(result)

        error = 'N'

    elif operation == '/':
        print("division")
        result = firstnumber/secondnumber
        print(result)
        error = 'N'
    elif operation == '-':
        print('substration')
        result = secondnumber-firstnumber
        print(result)
        error = 'N'
    elif operation == '+':
        print('sum')
        result=firstnumber+secondnumber
        print(result)
        error = 'N'
    else:
        print("please select a valid operation")
        operation = input(lista)
        error = 'Y'





