#Vai receber um número e verificar se ele é par ou ímpar

def obter_numero(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: A entrada não é um número inteiro válido.")

def verificar_paridade(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

numero = obter_numero("Digite um número inteiro: ")
paridade = verificar_paridade(numero)
print(f"O número {numero} é {paridade}.")



