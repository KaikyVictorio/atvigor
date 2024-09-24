from operacoes import somar, subtrair

a = int(input("Insira o primeiro numero"))
b = int(input("Insira o segundo número"))

perg= input("Quer somar[1] ou subtrair[2]?")

if perg == "1":
    print(somar(a,b))
if perg== "2":
    print(subtrair(a,b))

