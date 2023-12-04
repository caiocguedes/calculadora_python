from funcoes import *
import os

print("=================================================================")
print("SEJA BEM-VINDO À CALCULADORA!")
print("DESEJA REALIZAR UMA OPERAÇÃO? ")

opcao = int(input("1 - SIM    0 - NÃO: \n"))

while True:
    if opcao == 1:
        os.system("cls")
        print("==========================")
        print("Qual operação deseja realizar? \n")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Raiz quadrada")
        print("6 - Exponenciação \n")
        operacao = int(input(""))
        
        os.system("cls")
        
        match operacao:
            case 1:
                num1 = int(input("Adição selecionada! Digite o primeiro número: \n"))
                num2 = int(input("Agora digite o segundo número: \n"))
                resultado = somar(num1,num2)
                print("O resultado de {} + {} é {}".format(num1,num2, resultado))
            case 2:
                num1 = int(input("Subtração selecionada! Digite o primeiro número: \n"))
                num2 = int(input("Agora digite o segundo número: \n"))
                resultado = subtrair(num1,num2)
                print("O resultado de {} - {} é {}".format(num1,num2, resultado))
            case 3:
                num1 = int(input("Multiplicação selecionada! Digite o primeiro número: \n"))
                num2 = int(input("Agora digite o segundo número: \n"))
                resultado = multiplicar(num1,num2)
                print("O resultado de {} x {} é {}".format(num1,num2, resultado))
            case 4:
                num1 = int(input("Divisão selecionada! Digite o primeiro número: \n"))
                num2 = int(input("Agora digite o segundo número: \n"))   
                resultado = dividir(num1,num2) 
                print("O resultado de {} / {} é {}".format(num1,num2, resultado))
            case 5:
                num1 = int(input("Raiz quadrada selecionada! Digite o número: \n"))
                resultado = raiz_quadrada(num1)
                print("O resultado da raiz quadrada de {} é {}".format(num1, resultado))
            case 6:
                num1 = int(input("Exponenciação selecionada! Digite o primeiro número: \n"))
                num2 = int(input("Gostaria de elevá-lo a quanto? \n"))
                resultado = exponenciar(num1,num2)
                print("O resultado da exponenciação de {} por {} é {}".format(num1,num2, resultado))    
    print("================================================")    
    opcao = int(input("DESEJA REALIZAR OUTRA OPERAÇÃO? \n"))
    if opcao == 0:
        os.system("cls")
        print("Obrigado por utilizar a calculadora!")
        break
    elif opcao != 0 and opcao != 1:
        print("Opção inválida. Selecione '1' para uma nova operação ou '0' para sair.")     






