class Pai:
    def __init__(self, nome, peso, altura ):
        self.__nome = nome
        self.__peso = peso
        self.__altura = altura

    # Getters
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_peso(self):
        return self.__peso

    def get_altura(self):
        return self.__altura

    # Setters

    def set_peso(self, peso):
        self.__peso = peso

    def set_altura(self, altura):
        self.__altura = altura

    def exibirDados(self):
        print(f'Nome: {self.get_nome()}')
        print(f"Peso: {self.get_peso()} kg")
        print(f"Altura: {self.get_altura()} m")

class Mae:
    def __init__(self, nome, cabelo, corOlhos):
        self.__nome = nome
        self.__cabelo = cabelo
        self.__corOlhos = corOlhos

    # Getters
    def get_nome(self):
        return self.__nome
    def get_cabelo(self):
        return self.__cabelo

    def get_corOlhos(self):
        return self.__corOlhos

    # Setters
    def set_nome(self, nome):
        self.__nome = nome

    def set_cabelo(self, cabelo):
        self.__cabelo = cabelo

    def set_corOlhos(self, corOlhos):
        self.__corOlhos = corOlhos

    def exibirDados(self):
        print(f'Nome: {self.get_nome()}')
        print(f"Cabelo: {self.get_cabelo()}")
        print(f"Cor dos Olhos: {self.get_corOlhos()}")

class Filho(Pai, Mae):
    def __init__(self,nome, peso, altura, cabelo, corOlhos):
        Pai.__init__(self, nome, peso, altura)
        Mae.__init__(self, nome, cabelo, corOlhos)

    def exibirDados(self):
        print(f'Nome: {self.get_nome()}')
        print(f"Peso: {self.get_peso()} kg")
        print(f"Altura: {self.get_altura()} m")
        print(f"Cabelo: {self.get_cabelo()}")
        print(f"Cor dos Olhos: {self.get_corOlhos()}")