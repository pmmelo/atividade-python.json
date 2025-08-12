numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def filtrar_impares(lista):
    impares = []
    for numero in lista:
        if numero % 2 != 0:  # Verifica se é ímpar
            impares.append(numero)
    return impares


print(filtrar_impares(numeros))
