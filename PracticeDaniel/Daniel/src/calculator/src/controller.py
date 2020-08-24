# from module.function import sum, substraction, divide, multiply
# puedes traerte todas las funciones o funciones especificas

import module.function


def run_script():
    number_a = int(input('Enter a number:'))
    number_b = int(input('Enter another number:'))
    operation = input('What operation do you want to do? 1 sum, 2 multiply, 3-substraction, 4 division')
    # variable = "Pruebaaaa"
    # cualquier_string = ("esto" + "otra cosa" + variable)
    # alternativa = f"la variable va aqui {variable}"
    if operation == "1":
        print(sum(number_a, number_b))
    elif operataion == "2"
        print(multiplication(number_a, number_b)
    elif operation == "3"
        print(substraction(number_a, number_b))
    elif operation == "4"
        print(divide(number_a, number_b))





