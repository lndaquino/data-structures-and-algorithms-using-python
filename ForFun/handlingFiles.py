#abre arquivo para escrita
arq = open('file.txt', 'w')

#msg para ser escrita no arquivo
msg = '''Esse é um exemplo
de mensagem que escreverei
no arquivo
'''

#escrevendo no arquivo
arq.write(msg)

#fecha o arquivo
arq.close()

#abrindo o arquivo para leitura
file = open('file.txt', 'r')

#imprimindo o texto do arquivo
print(''.join(linha for linha in file.readlines()))

file.close()