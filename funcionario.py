import math
class Funcionario:
    def __init__(self,id_funcionario, nome, cpf, cargo, salario):

        if type(id_funcionario) is not int:
            raise TypeError("O número da matrícula deve ser inteiro!")
        if id_funcionario <= 0:
            raise ValueError("O número de matrícula deve ser maior que 0")
        self.id_funcionario = id_funcionario
        
        
       

        nome = nome.strip()
        if not nome:
            raise ValueError("É obrigatório o preenchimento do nome!")
        self.nome = nome

        cpf = str(cpf).strip()
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError("É obrigatório o preenchimento do CPF com 11 dígitos!")
        self.cpf = cpf


        cargo = cargo.lower().strip()
        if not cargo:
            raise ValueError("É obrigatório o preenchimento do cargo!")
        self.cargo = cargo

        salario = float(salario)
        if salario <= 0:
            raise ValueError("O valor do salário deve ser maior que zero!")
        if not math.isfinite(salario):
            raise ValueError("O valor do salário deve ser finito!")
        self.salario = salario
        
        self.ativo = True

    def exibir_dados(self):
        return f"{self.id_funcionario} | {self.nome} | {self.cpf} | {self.cargo} | {self.salario} | {self.ativo}"

