def esta_vazia(lista):
    return not lista

def criar_lista():
    lista = []
    print("Digite os valores para a lista. Quando quiser parar, digite ENTER sem nada.")
    while True:
        valor = input("Digite um valor: ")
        if valor == "":
            break
        lista.append(valor)
    return lista

minha_lista = criar_lista()
resultado = esta_vazia(minha_lista)
print(f"A lista que você criou é: {minha_lista}")
print(f"A lista está vazia? {resultado}")
