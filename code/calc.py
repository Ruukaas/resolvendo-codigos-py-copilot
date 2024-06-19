#Vai receber dois números inteiros e realizar uma operação simples entre eles
print("Desafio 3 - Operações Matemáticas Simples\n")

def obter_numero(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: A entrada não é um número inteiro válido.")


def escolher_operacao():
    print("Escolha a operação:")
    print("1: Adição")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    while True:
        operacao = input("Digite o número da operação desejada: ")
        if operacao in ['1', '2', '3', '4']:
            return operacao
        else:
            print("Erro: Operação inválida. Escolha 1, 2, 3 ou 4.")

num1 = obter_numero("Digite o primeiro número inteiro: ")
num2 = obter_numero("Digite o segundo número inteiro: ") 

operacao = escolher_operacao()

if operacao == '1':
        resultado = num1 + num2
        print(f"Resultado da adição: {num1} + {num2} = {resultado}")
elif operacao == '2':
        resultado = abs(num1 - num2)
        print(f"Resultado da subtração absoluta: |{num1} - {num2}| = {resultado}")
elif operacao == '3':
        resultado = num1 * num2
        print(f"Resultado da multiplicação: {num1} * {num2} = {resultado}")
elif operacao == '4':
    if num2 == 0:
        print("Erro: Divisão por zero não é permitida.")
    else:
        quociente = num1 // num2
        resto = num1 % num2
        print(f"Resultado da divisão: {num1} / {num2} = {quociente} com resto {resto}")