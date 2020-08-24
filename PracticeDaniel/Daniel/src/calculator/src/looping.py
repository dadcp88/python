def count_to_10():
    for i in range (1,11):
        print(i)

#recorrer el item en la lista

def loop_a_list(lista):
    #el for para cada item (es un nombre de variable X) y la lista
    for item in lista:
        print(item)

def loop_a_dictionary(dictionary):
    for key in dictionary:
        print ("este es el key:", key, "Este es el value:", dictionary [key])

def loop_string(word):
    for letter in word:
        print(letter)

def string_operations(word):
    print(word[:5])
    print(word[2:])
    print(word[2:5])

if __name__ == '__main__':
    count_to_10()
    loop_a_list(['leo', 'mari', 'daniel'])
    loop_a_dictionary({'name' : 'daniel'})
    loop_string('daniel')
    string_operations("greenday")