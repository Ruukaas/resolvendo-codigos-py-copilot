#Vai receber uma String e um número inteiro como entrada, depois vai retornar a String a quantidade de vezes do inteiro

print("Desafio 2 - Repetindo Textos\n")

text = input("Insira a frase que vai ser repetida:")
loop = input("Insira a quantidade de vezes que o número vai ser repetido:")

try:
    numero = int(loop)
    print((text + "\n") * numero)
except ValueError:
    print("Erro: A entrada não é um número inteiro válido.")

