from funcionario import Funcionario
def test_nome():
    funcionario = Funcionario(1, "Antonio","00000000000", "gerente", 3100.00)

    assert funcionario.nome == "Antonio"

def test_salario():
    funcionario = Funcionario(2,"Arthur", "12345678910", "analista", 4000.00)
    assert type(funcionario.salario) == float

def test_ativo():
    funcionario = Funcionario(3,"Arthur", "12345678910", "analista", 4000.00)
    assert funcionario.ativo == True
