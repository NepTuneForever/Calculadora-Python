import time


def calcular(numero1, numero2, operacao):
    operacoes = {
        "+": numero1 + numero2,
        "-": numero1 - numero2,
        "*": numero1 * numero2,
        "**": numero1 ** numero2
    }
    return operacoes.get(operacao, None) 


while True:
    try:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        break  # Sai do loop se a entrada for válida
    except ValueError:
        print("Erro! Digite apenas números inteiros.")

print("\nOpções de operações: +, -, *, **")


while True:
    operacao = input("Digite uma das opções acima: ")
    resultado = calcular(numero1, numero2, operacao)

    if resultado is not None:
        break 
    print("Operação inválida! Tente novamente.")

print("\nCalculando resultado...")
time.sleep(1)

print(f"O resultado de {numero1} {operacao} {numero2} é: {resultado}")
