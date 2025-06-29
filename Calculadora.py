def soma(x, y):
    return x + y
def subtracao(x, y):
    return x - y
def multiplicacao(x, y):
    return x * y
def divisao(x, y):
    if(y == 0):
        print("Erro! Divisão por zero")
        return None
    return x / y
    
print("(1) - Soma (2) - Subtração \n (3) - Multiplicação (4) - Divisão")
operacao = int(input("Qual operação você quer utilizar?: "))
x = float(input("Digite o valor de X: "))
y = float(input("Digite o valor de Y: "))

if(operacao == 1):
    print("A Soma de X e Y é:", soma(x, y))
elif(operacao == 2):
    print("A Subtração de X e Y é:", subtracao(x, y))
elif(operacao == 3):
    print("A Multiplicação de X e Y é:", multiplicacao(x, y))
elif(operacao == 4):
    resultado = divisao(x, y)
    if(resultado is not None):
        print("A Divisão de X e Y é:", resultado)
else:
    print("Escolha inválida!")