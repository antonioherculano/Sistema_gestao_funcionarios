from funcionario import Funcionario
try:
    funcionario1 = Funcionario(1.1, "Antonio","00000000000", "gerente", 3100.00)
except TypeError as erro:
    print(f"1. Erro no cadastro: {erro}")
else:
    print("1. Teste positivo! Sem erros!")

try:
    funcionario2 = Funcionario(2,"Arthur", "12345678910", "analista", 4000.00)
except (TypeError, ValueError) as erro:
    print(f"2. Erro no cadastro: {erro}")
else:
    print("2. Teste positivo! Sem erros!")

try:
    funcionario3 = Funcionario(3,"Arthur", "12345678910", "analista", "nan")
except ValueError as erro:
    print(f"3. Erro no cadastro: {erro}")
else:
    print("3. Teste positivo! Sem erros!")


try:
    funcionario4 = Funcionario(4,"Arthur", "12345678910", "analista", 0)
except ValueError as erro:
    print(f"4. Erro no cadastro: {erro}")
else:
    print("4. Teste positivo! Sem erros!")

