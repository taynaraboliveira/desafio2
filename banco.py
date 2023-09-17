import sqlite3
conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

# Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
result = cursor.execute('''
    CREATE TABLE alunos (
        id INTEGER,
        nome VARCHAR(250),
        idade INTEGER,
        curso VARCHAR(250)
    )
''')

# Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
result = cursor.executemany('''
    INSERT INTO alunos (id, nome, idade, curso) VALUES (?, ?, ?, ?)
''', [
    (1, 'Camila', 20, 'Dados'),
    (2, 'Maria', 22, 'Dados'),
    (3, 'Joana', 24, 'Engenharia'),
    (4, 'Clara', 25, 'Dados'),
    (5, 'Simone', 30, 'Engenharia')
])

# Consultas Básicas

# a) Selecionar todos os registros da tabela "alunos".
result = cursor.execute('SELECT * FROM alunos')
print(cursor.fetchall())

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
result = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
print(cursor.fetchall())

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
result = cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome')
print(cursor.fetchall())

# d) Contar o número total de alunos na tabela.
result = cursor.execute('SELECT COUNT(*) FROM alunos')
print(cursor.fetchone()[0])

# Atualização e Remoção

# a) Atualize a idade de um aluno específico na tabela.
result = cursor.execute('UPDATE alunos SET idade = 28 WHERE id = 1')

# b) Remova um aluno pelo seu ID.
result = cursor.execute('DELETE FROM alunos WHERE id = 1')

# 5. Criar uma Tabela e Inserir Dados

# Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float).
result = cursor.execute('''
    CREATE TABLE clientes (
        id INTEGER PRIMARY KEY,
        nome VARCHAR(250),
        idade INTEGER,
        saldo FLOAT
    )
''')

# Insira alguns registros de clientes na tabela.
result = cursor.executemany('''
    INSERT INTO clientes (id, nome, idade, saldo) VALUES (?, ?, ?, ?)
''', [
    (1, 'Camila', 20, 1000.0),
    (2, 'Maria', 33, 200.0),
    (3, 'Joana', 24, 500.0),
    (4, 'Clara', 40, 1200.0),
    (5, 'Simone', 30, 300.0)
])

# 6. Consultas e Funções Agregadas

# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
result = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
print(cursor.fetchall())

# b) Calcule o saldo médio dos clientes.
result = cursor.execute('SELECT AVG(saldo) FROM clientes')
print(cursor.fetchone()[0])

# c) Encontre o cliente com o saldo máximo.
result = cursor.execute('SELECT nome FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')
print(cursor.fetchall())

# d) Conte quantos clientes têm saldo acima de 1000.
result = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
print(cursor.fetchone()[0])

# 7. Atualização e Remoção com Condições

# a) Atualize o saldo de um cliente específico.
result = cursor.execute('UPDATE clientes SET saldo = 2000 WHERE id = 1')

# b) Remova um cliente pelo seu ID.
result = cursor.execute('DELETE FROM clientes WHERE id = 1')

# 8. Junção de Tabelas

# Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"),
# produto (texto) e valor (real).
result = cursor.execute('''
    CREATE TABLE compras (
        id INTEGER PRIMARY KEY,
        cliente_id INTEGER,
        produto VARCHAR(250),
        valor FLOAT,
        FOREIGN KEY (cliente_id) REFERENCES clientes (id)
    )
''')

# Insira algumas compras associadas a clientes existentes na tabela "clientes".
result = cursor.executemany('''
    INSERT INTO compras (id, cliente_id, produto, valor) VALUES (?, ?, ?, ?)
''', [
    (1, 1, 'Caderno', 20.0),
    (2, 1, 'Caneta', 1.10),
    (3, 2, 'Caderno', 24.0)
])

# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra
result = cursor.execute('''
    SELECT clientes.nome, compras.produto, compras.valor 
    FROM compras 
    INNER JOIN clientes ON compras.cliente_id = clientes.id
''')

for row in cursor.fetchall():
    print(row)

conexao.commit()
conexao.close()