class Pessoa:
    def __init__(self, nome, peso, nacionalidade, idade, sexo):
        self.nome = nome
        self.peso = peso
        self.nacionalidade = nacionalidade
        self.idade = idade
        self.sexo = sexo

def escolher_nomes(lista_objetos):
    print("Lista de pessoas disponíveis:")
    for i, obj in enumerate(lista_objetos):
        print(f"{i}: {obj.nome} - {obj.peso}kg, {obj.nacionalidade}, {obj.idade} anos, {obj.sexo}")
    
    escolhas = input("Digite os índices das pessoas que quer escolher, separados por vírgula: ")
    indices = []
    for x in escolhas.split(","):
        x = x.strip()
        if x.isdigit():
            idx = int(x)
            if 0 <= idx < len(lista_objetos):
                indices.append(idx)
            else:
                print(f"Índice {idx} ignorado (fora do intervalo).")
        else:
            print(f"Entrada '{x}' ignorada (não é número).")
    
    nomes_escolhidos = [lista_objetos[i].nome for i in indices]
    return nomes_escolhidos


    nomes = escolher_nomes(pessoas)
    print("Nomes escolhidos:", nomes)
