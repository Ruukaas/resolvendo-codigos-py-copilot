#Vai receber uma palavra e inverter ela para ver se é igual
def verificar_palindromo(texto):
    texto = texto.replace(" ", "").lower()

    # Esta é uma forma de fatiamento de strings (string slicing) em Python.
    #O formato geral para fatiamento é string[início:fim:passo].
    #Quando usamos [::-1], estamos utilizando:
    #Início: Em branco, o que significa que começa do início da string.
    #Fim: Em branco, o que significa que vai até o fim da string.
    #Passo: -1, que indica que a string deve ser lida de trás para frente.
    
    return texto == texto[::-1]

entrada = input("Digite um texto para verificar se é um palíndromo: ")
    
if verificar_palindromo(entrada):
    print(f'"{entrada}" é um palíndromo.')
else:
    print(f'"{entrada}" não é um palíndromo.')


