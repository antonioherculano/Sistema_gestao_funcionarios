# Sistema de Gestão de Funcionários

**Status:** em desenvolvimento — etapa 1: modelagem e validação de funcionários.

Sistema de cadastro de funcionários desenvolvido em Python, com foco em
orientação a objetos, validação de dados e testes automatizados.

O projeto surgiu da minha experiência profissional em um escritório de
terceirização de mão de obra, onde observo frequentemente como informações
incorretas, como um CPF inválido ou um salário digitado errado, podem
comprometer as etapas seguintes dos processos administrativos.

O objetivo é desenvolver o sistema de forma incremental, aplicando conceitos de
programação e práticas como testes automatizados e versionamento com Git
conforme avanço nos estudos.

## Etapa atual: modelagem do funcionário

Nesta primeira etapa, desenvolvi a classe `Funcionario`, responsável por
representar um funcionário e validar seus dados no momento da criação.

Para que um funcionário seja criado, é necessário que:

* A matrícula seja um número inteiro maior que zero;
* O CPF contenha exatamente 11 dígitos numéricos;
* O nome e o cargo estejam preenchidos;
* O salário seja um número finito e maior que zero.

A classe também possui o atributo `ativo`, que indica se o funcionário está em
atividade e será utilizado futuramente no desligamento de funcionários.

## Decisões de implementação

### Centralização das validações

As validações foram concentradas no método `__init__`, o que impede a criação
de funcionários com dados inválidos e evita repetir essas regras nas próximas
etapas do projeto.

### Tratamento de exceções

Utilizei dois tipos de exceções:

* `TypeError`: quando a matrícula informada não é do tipo inteiro;
* `ValueError`: quando um valor não atende às regras estabelecidas.

Essa separação permite identificar melhor a origem dos erros durante a execução.

### Validação de valores especiais

Durante os testes, identifiquei que `float("nan")` passava pela verificação
inicial de salário, pois comparações de ordem com `nan` retornam `False`.

Para corrigir esse comportamento, utilizei `math.isfinite()`, que permite
rejeitar valores como `nan` e infinito.

## Como executar

O projeto utiliza Python 3.

Para executar os exemplos de cadastro e validação:

```bash
python3 main.py
```

Para executar os testes automatizados, após instalar o `pytest`:

```bash
pytest -v
```

## Próximas etapas

1. Implementar cadastro e listagem de funcionários pelo terminal;
2. Adicionar pesquisa, edição e desligamento de funcionários;
3. Implementar persistência de dados em arquivos JSON;
4. Migrar o armazenamento para SQLite;
5. Desenvolver uma API para disponibilizar as funcionalidades;
6. Explorar a implantação do sistema em nuvem.