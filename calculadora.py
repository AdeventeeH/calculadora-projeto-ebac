## Criação de uma calculadora simples em Python com as operações básicas: adição, subtração, multiplicação e divisão.

## Função para informar o primeiro número
def obter_numero_1():
    while True:
        try:
            numero_1 = float(input("Digite o primeiro número: "))
            return numero_1
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

## Função para informar a operação desejada
def obter_operacao():
    while True:
        operacao = input("Digite a operação (+, -, *, /): ")
        if operacao in ['+', '-', '*', '/']:
            return operacao
        else:
            print("Operação inválida. Por favor, digite uma operação válida.")

## Função para informar o segundo número
def obter_numero_2():
    while True:
        try:
            numero_2 = float(input("Digite o segundo número: "))
            return numero_2
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

## Função para realizar a operação escolhida
def calcular(numero_1, operacao, numero_2):
    if operacao == '+':
        return numero_1 + numero_2
    elif operacao == '-':
        return numero_1 - numero_2
    elif operacao == '*':
        return numero_1 * numero_2
    elif operacao == '/':
        if numero_2 != 0:
            return numero_1 / numero_2
        else:
            return "Erro: Divisão por zero não é permitida."

## Função principal para executar a calculadora
def main():
    print("Calculadora Simples")
    print("-" * 20)

    numero_1 = obter_numero_1()
    operacao = obter_operacao()
    numero_2 = obter_numero_2()

    resultado = calcular(numero_1, operacao, numero_2)
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()

## Função que solicita se o usuário deseja realizar outra operação
def continuar():
    while True:
        resposta = input("Deseja realizar outra operação? (s/n): ").lower()
        if resposta in ['s', 'n']:
            return resposta == 's'
        else:
            print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")

## Modificação da função principal para permitir múltiplas operações
# A função main agora inclui um loop que permite ao usuário realizar várias operações sem precisar reiniciar o programa, e oferece a opção de encerrar a calculadora quando o usuário desejar.
def main():
    print("Calculadora Simples")
    print("-" * 20)

    # Loop para permitir que o usuário realize múltiplas operações
    while True:
        numero_1 = obter_numero_1()
        operacao = obter_operacao()
        numero_2 = obter_numero_2()

        # Realiza a operação e exibe o resultado
        resultado = calcular(numero_1, operacao, numero_2)
        print(f"Resultado: {resultado}")

        # Pergunta ao usuário se deseja realizar outra operação
        if not continuar():
            print("Obrigado por usar a calculadora. Até a próxima!")
            break

# O código agora permite que o usuário realize múltiplas operações sem precisar reiniciar o programa, e inclui uma opção para encerrar a calculadora quando o usuário desejar.
if __name__ == "__main__":
    main()

# Este código cria uma calculadora simples que solicita ao usuário dois números e a operação desejada, e então exibe o resultado da operação. Ele inclui tratamento de erros para entradas inválidas e divisão por zero.