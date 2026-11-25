class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base


class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus

    def calcular_salario(self):
        return super().calcular_salario() + self.bonus


class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, vendas, comissao=0.05):
        super().__init__(nome, salario_base)
        self.vendas = vendas
        self.comissao = comissao

    def calcular_salario(self):
        return super().calcular_salario() + self.vendas * self.comissao


funcionarios = [
    Funcionario("Ana", 2000),
    Gerente("Bruno", 4000, 1500),
    Vendedor("Carla", 1800, 20000),
]

for funcionario in funcionarios:
    print(f"{funcionario.nome}: R$ {funcionario.calcular_salario():.2f}")
