#Calculator Functions... Why not

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
        result = multiply(firstnumber, secondnumber)
        # write("hi")
        print(result)
        error = 'N'
        text_file = open(filename, "w")
        text_file.write(result)
        text_file.close()


    elif operation == '/':
        print("division")
        result = divide(firstnumber, secondnumber)
        print(result)
        error = 'N'
    elif operation == '-':
        print('substration')
        result = substraction(firstnumber, secondnumber)
        print(result)
        error = 'N'
    elif operation == '+':
        print('sum')
        result = add(firstnumber, secondnumber)
        print(result)
        error = 'N'
    else:
        print("please select a valid operation")
        operation = input(lista)
        error = 'Y'





