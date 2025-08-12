numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def valores_unicos(lista):
    vistos = set()
    unicos = []
    for item in lista:
        if item not in vistos:
            vistos.add(item)
            unicos.append(item)
    return unicos

resultado = valores_unicos(numeros)
print(resultado)
