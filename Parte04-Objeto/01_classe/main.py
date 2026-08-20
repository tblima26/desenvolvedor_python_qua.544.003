class Pessoa:
  #NOTE - método construtor
  def __init__(self,nome,idade,email,altura):
    self.nome = nome
    self.idade = idade
    self.email = email
    self.altura = altura

  #NOTE - método construtor
  def exibir(self):
    print(f"Nome: {self.nome}.")
    print(f"Idade: {self.idade} anos")
    print(f"E-mail: {self.email}.")
    print(f"Altura: {self.altura} metros")


def ler_string(mensagem):
    return input(mensagem).strip().lower()


def ler_float(mensagem):
    return float(input(mensagem).replace(",", "."))


def ler_int(mensagem):
    return int(input(mensagem))

def main():
  usuario = Pessoa("Maria", 28, "maria@email.com", 1.68)
  usuario2 = Pessoa(
     ler_string('Nome: ').title(),
     ler_int('Idade: '),
     ler_string('Email: '),
     ler_float('Altura: '),
  )
  print(f'{"=" * 25}')
  print('--- Exibir Dados ---')
  print(f'{"=" * 25}')
  usuario.exibir()
  print(f'{"=" * 25}')
  usuario2.exibir()

if __name__ == "__main__":
  main()
