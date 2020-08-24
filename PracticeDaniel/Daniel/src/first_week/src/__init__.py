# Variables
# Funciones
#las variables son interpretados, el type (variable) te da el tipo de dato que esta interpretando.

number = 2
lista = ['a', 'b', 'c']
# control / es para comentar, append es para ingresar la informacion dentro de la lista

lista.append(['a', 'b', 'c'])
# lista.remove() #hashable, mutable
lista.append("a")
lista.append("b")
lista.append("c")

lista[0]=2


print(type(number), number)
print(type(lista), lista)

# Tuple no recuerda las posiciones pero es mucho mas rapida que la lista.
tuple = ('a', 'b', 'c')
#tuple[0] = 1 #no se puede, ya que no soporte asignacion de item, tuple no guarda las posiciones.

print(type(tuple), tuple)

diccionario = {
    'name': 'daniel',
    'pet': {
    'name': 'lilly'}
}

print(type(diccionario), diccionario['name'])


persona = {
    'name': {
        'First_name': 'daniel',
        'last_name': 'De Crescenzo'
    },
    'address': {
        'address_1': 'Panama',
        'address_2': 'San Francisco',
        'address_lista': ['address1 lista', 'address2 lista', 'address3 lista']
    },
    'work': {
        'type': 'it support'
    }
}

print(type(persona), persona['work'])
print(type(persona), persona['address']['address_1'])
print(type(persona), persona['address']['address_2'])
print(type(persona), persona['address']['address_lista'][1])
persona.update({'hobbies': {1: 'tejer'}, 2: 'cocinar'})

persona['name']['first_name'] = 'daniel2'
print(type(persona), persona)

# pprint package

# if __name__ == '__main__'