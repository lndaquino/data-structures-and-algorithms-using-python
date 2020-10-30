from tkinter import *
import tkinter.filedialog as filedialog
from tkinter import messagebox

nome_arquivo = 'my_file.txt'

def novo_arquivo():
  text_box.delete(0.0, END)

def salvar_arquivo():
  text = text_box.get(0.0, END)
  arquivo = open(nome_arquivo, 'w')
  arquivo.write(text)
  arquivo.close()

def salvar_como():
  arquivo = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
  if arquivo != None:
    text = text_box.get(0.0, END)
    try:
      arquivo.write(text.rstrip())
    except:
      messagebox.showerror(title = "Erro", message = 'Não foi possível salvar o arquivo')

def abrir_arquivo():
  arquivo = filedialog.askopenfile(mode = 'r')
  if arquivo != None:
    text = arquivo.read()
    text_box.delete(0.0, END)
    text_box.insert(0.0, text)


largura, altura = 800, 600
janela = Tk()
janela.title('PyNotePad')
janela.minsize(width = largura, height = altura)
janela.maxsize(width = largura, height = altura)

text_box = Text(janela, width = largura, height = altura)
text_box.pack()

menu_bar = Menu(janela)

file_menu = Menu(menu_bar)
file_menu.add_command(label = 'Novo', command = novo_arquivo)
file_menu.add_command(label = 'Abrir', command = abrir_arquivo)
file_menu.add_command(label = 'Salvar', command = salvar_arquivo)
file_menu.add_command(label = 'Salvar como...', command = salvar_como)
file_menu.add_separator()
file_menu.add_command(label = 'Sair', command = janela.quit)

menu_bar.add_cascade(label = 'Arquivo', menu = file_menu)

janela.config(menu = menu_bar)
janela.mainloop()