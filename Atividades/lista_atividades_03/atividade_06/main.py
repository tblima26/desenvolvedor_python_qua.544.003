from models import Pessoa, Conta
import service as s

def menu():
    print(f'{"="*30}')
    print("       SISTEMA BANCÁRIO       ")
    print(f'{"="*30}')
    print("[1] Consultar Dados da Conta")
    print("[2] Depositar")
    print("[3] Sacar")
    print("[4] Gerar Extrato (.txt)")
    print("[0] Sair")
    print(f'{"="*30}')
    opcao = int(input("Escolha uma opção: "))
    return opcao

def criarPessoa():
    s.limpar()
    print("=== CADASTRO DA PESSOA ===")
    nome = s.lerString("Nome: ")
    cpf = s.lerString('Cpf: ') # Adicionado os dois pontos para padronizar
    return Pessoa(nome=nome, cpf=cpf)
     
def main():
    usuario = criarPessoa()
    conta = Conta(usuario=usuario, agencia="0014", conta="12345-6", saldo=0.0)
    
    while True:
        s.limpar()
        opcao = menu()   
        s.limpar()
        match opcao:
            case 1:
                conta.consultarDados()
            case 2:
                valor = s.lerFloat('Depositar: R$ ')
                conta.depositar(valor)
                print(f"Depósito realizado! Saldo atual: R$ {conta.saldo:.2f}")
            case 3:
                valor = s.lerFloat('Sacar: R$ ')
                if valor <= conta.saldo:
                    conta.sacar(valor)
                    print(f"Saque realizado! Saldo atual: R$ {conta.saldo:.2f}")
                else:
                    print("❌ Saldo insuficiente!")
            case 4:
                conta.gerarExtrato()
            case 0:
                print("Saindo do sistema... Até logo!")
                break
            case _:
                print("❌ Opção inválida!")
        
        # Pausa para o usuário conseguir ler a mensagem antes da tela limpar de novo
        if opcao != 0:
            input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    main()