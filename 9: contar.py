numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
def contar_ocorrencias_interativo(lista):
    print("Lista:", lista)
    valor_str = input("Digite o número que você quer contar na lista: ")
    try:
        valor = int(valor_str)
    except ValueError:
        print("Valor inválido! Por favor, digite um número inteiro.")
        return None
    
    total = lista.count(valor)
    print(f"O valor {valor} aparece {total} vezes na lista.")
    return total

contar_ocorrencias_interativo(numeros)
