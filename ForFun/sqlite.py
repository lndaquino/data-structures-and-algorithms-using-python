import sqlite3

#criando uma conexão com o banco passando o nome do arquivo
conn = sqlite3.connect('myDatabase.DB')
#obtendo um cursor
c = conn.cursor()
#função para criar a tabela
def createTable():
  c.execute('CREATE TABLE IF NOT EXISTS cars(name TEXT, year INTEGER, price REAL)')

#função para inserir registro na tabela
def insertEntry(name, year, price):
  c.execute("INSERT INTO cars (name, year, price) values (?, ?, ?)", (name, year, price))
  conn.commit()

#função para mostrar todos os registros
def showAll():
  print('\nExibindo todos os registros:\n')
  c.execute('SELECT * FROM cars')
  rows = c.fetchall()

  for row in rows:
    print(row)


#função para mostrar um único registro pelo nome
def showRegister(name):
  print('\nExibindo o registro %s\n' % name)
  c.execute("SELECT name, year, price FROM cars WHERE name=:name", {"name": name})
  row = c.fetchone()
  if row:
    print(row)
  else:
    print('Registro não encontrado')

#função para atualizar o nome dos registros
def updateName(oldName, newName):
  c.execute("UPDATE cars SET name=? WHERE name=?", (newName, oldName))


#cria a tabela
createTable()
#insere os registros
insertEntry('Camaro', 2016, 200000)
insertEntry('Jaguar', 2018, 600000)
insertEntry('Azera', 2020, 120000)
insertEntry('Spin', 2012, 56000)

showAll()

showRegister('Azera')

updateName('Camaro', 'Caramelo')

showAll()

#fecha o cursor e a conexão
c.close()
conn.close()