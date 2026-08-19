'''
#TODO - 
- Utiliza recursividade para desenvolver um programa onde o usuário fornece um número inteiro.
- O sistema calcula e exibe a sequência de Fibonacci até o termo correspondente ao número informado.
'''
import modulo as m

def main():
    m.limpar()
    print("--- Sequência de Fibonacci (Recursiva) ---")
    lista = []
    n = m.lerInteiro("Quantidade de termos da sequência: ")
    if n <= 0:
        print("Por favor, informe um número inteiro maior que zero.")
    else:
        print(f"\nSequência de Fibonacci até o {n}º termo:")
        for i in range(n):
            lista.append(m.fibonacci(i))
        print(lista)

    print(f"\n\nNúmero de ouro:")
    for i in range(len(lista) -1):
        nominador = lista[i+1]
        denominador = lista[i]
        if denominador == 0:
            resultado = 0.0
        else:
            resultado = nominador / denominador
        print(f"{nominador} / {denominador} = {resultado:.5f}")

    print(f"\n\Proporção Aurea:")
    for i in range(len(lista) -1):
        nominador = lista[i]
        denominador = lista[i+1]
        if denominador == 0:
            resultado = 0.0
        else:
            resultado = nominador / denominador
        print(f"{nominador} / {denominador} = {resultado:.5f}")

if __name__ == "__main__":
    main()