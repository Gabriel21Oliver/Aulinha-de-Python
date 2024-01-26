# Aulinha-de-Python
import math

def calculadora_cientifica():
    print("Calculadora Científica Simples")
    print("Operações disponíveis: +, -, *, /, sqrt, sin, cos, tan, log")

    while True:
        try:
            operacao = input("Digite a operação (ou 'sair' para encerrar): ").lower()

            if operacao == 'sair':
                print("Calculadora encerrada.")
                break

            if operacao in ('sqrt', 'sin', 'cos', 'tan', 'log'):
                numero = float(input("Digite o número: "))
                resultado = getattr(math, operacao)(numero)
            else:
                numero1 = float(input("Digite o primeiro número: "))
                numero2 = float(input("Digite o segundo número: "))

                if operacao == '+':
                    resultado = numero1 + numero2
                elif operacao == '-':
                    resultado = numero1 - numero2
                elif operacao == '*':
                    resultado = numero1 * numero2
                elif operacao == '/':
                    resultado = numero1 / numero2
                else:
                    print("Operação inválida.")
                    continue

            print("Resultado:", resultado)

        except ValueError:
            print("Por favor, insira números válidos.")
        except ZeroDivisionError:
            print("Divisão por zero não é permitida.")

if __name__ == "__main__":
    calculadora_cientifica()
