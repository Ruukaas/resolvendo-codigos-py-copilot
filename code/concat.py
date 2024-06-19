#Vai receber dados e concatenar eles até receber a flag --1
print("Desafio 1 - Concatenando Dados\n")

entradas = []

while True:
    entrada = input("Digite uma entrada(ou --1) para terminar:")

    if(entrada == "--1"):
        break

    entradas.append(entrada)
    
resultConcat = " ".join(entradas)

print("A string concatenada é:", resultConcat)
