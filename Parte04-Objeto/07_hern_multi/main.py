from models import Mae,Pai,Filho
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    limpar_tela()
    print("--- Testando o Pai ---")
    pai = Pai("Carlos", 80.5, 1.75)
    pai.exibirDados()

    print("\n--- Testando a Mãe ---")
    mae = Mae("Ana", "Loiro", "Azuis")
    mae.exibirDados()
    print("\n--- Testando o Filho (Herança Múltipla) ---")
    filho = Filho("Lucas", 45.0, 1.50, "Castanho", "Castanhos")
    filho.exibirDados()
    

if __name__ == '__main__':
    main()