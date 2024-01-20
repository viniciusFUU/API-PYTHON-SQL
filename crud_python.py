import mysql.connector

conexao = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    password = '3905281328',
    database = 'bd_api_python'
)

cursor = conexao.cursor()

#create
# nome_produto = input("DIgite o nome do produto: ")
# valor = int(input("Valor do produto: "))

# comando_creat = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
# cursor.execute(comando_creat)
# conexao.commit() #caso mude algo no banco de dados


# read
# comando_read = 'SELECT * FROM vendas'
# cursor.execute(comando_read)
# resultado = cursor.fetchall()
# print(resultado)


#update
# novo_nome_produto = input("Digite o nome do produto que irá alterar o valor: ")
# novo_valor = int(input("Digite o novo valor do produto: "))
# comando_update = f'UPDATE vendas SET valor = {novo_valor} WHERE nome_produto = "{novo_nome_produto}"'
# cursor.execute(comando_update)
# conexao.commit()


#delete
nome_deletado = input("Digite o produto que você deseja deletar: ")
comando_delete = f'DELETE FROM vendas WHERE nome_produto = "{nome_deletado}"'
cursor.execute(comando_delete)
conexao.commit()

cursor.close()
conexao.close()