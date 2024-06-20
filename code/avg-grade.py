#Vai pedir a quantidade de notas que serão inseridas, pedir para que insira elas e tirar a média aritmética das mesmas

def obter_numero_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: A entrada não é um número inteiro válido.")

def obter_numero_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: A entrada não é um número válido. Tente novamente.")

quantidade_notas = obter_numero_inteiro("Digite a quantidade de notas que serão inseridas: ")

notas = []

    
for i in range(quantidade_notas):
    nota = obter_numero_float(f"Digite a nota {i+1}: ")
    notas.append(nota)

media = sum(notas) / quantidade_notas

print(f"A média aritmética das notas inseridas é: {media:.2f}")

