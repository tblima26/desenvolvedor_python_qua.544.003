'''
#REVIEW
'''

import os

def main():
    print("--- Automatizador de Git ---")
    
    # 1. Pergunta a mensagem do commit usando input()
    mensagem = input("Digite a mensagem do commit: ")
    
    if not mensagem.strip():
        print("A mensagem do commit não pode estar vazia. Cancelando.")
        return

    print("\nExecutando comandos do Git...")
    
    # 2. Executa os comandos do git usando o os.system
    os.system("cd ..")
    os.system("cd ..")
    os.system("git add .")
    os.system(f'git commit -m "{mensagem}"')
    os.system("git push")
    
    print("\n Projeto atualizado e enviado para o Git com sucesso!")

if __name__ == "__main__":
    main()