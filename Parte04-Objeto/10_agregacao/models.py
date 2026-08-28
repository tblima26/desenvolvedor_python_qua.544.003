class Departamento:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome


class Empresa:
    def __init__(self, nome, departamento):
        self.__nome = nome
        self.__departamento = departamento

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_departamento(self):
        return self.__departamento

    def set_departamento(self, departamento):
        self.__departamento = departamento

    def detalhes(self):
        return f"Empresa: {self.__nome}\nDepartamento: {self.__departamento.get_nome()}"