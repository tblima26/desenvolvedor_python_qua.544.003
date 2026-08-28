class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Erro: Divisão por zero!"
        return a / b


class Pedido:
    def __init__(self, v1, v2):
        self.__v1 = v1
        self.__v2 = v2

    def get_v1(self):
        return self.__v1

    def set_v1(self, v1):
        self.__v1 = v1

    def get_v2(self):
        return self.__v2

    def set_v2(self, v2):
        self.__v2 = v2


    def calcular_total(pedido, operador):
        calc = Calculadora()
        v1 = pedido.get_v1()
        v2 = pedido.get_v2()

        match operador:
            case 1:
                return calc.somar(v1, v2)
            case 2:
                return calc.subtrair(v1, v2)
            case 3:
                return calc.multiplicar(v1, v2)
            case 4:
                return calc.dividir(v1, v2)
            case _:
                return "Opção inválida! Escolha de 1 a 4 ou use +, -, *, /"