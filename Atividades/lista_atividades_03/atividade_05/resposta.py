def fibonacci(n):
    return n if n<=1 else fibonacci(n-1) + fibonacci(n-2)

def main():
    n = int(input('Numero inteiro: '))
    print(f'O numero da sequencia de fibonacci: {fibonacci(n)}')
    

if __name__ == "__main__":
    main()