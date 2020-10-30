from tkinter import *
from facePhoto import *
from PIL import Image, ImageTk

window = Tk() #cria uma janela
window.title('Facebook profile photo') #seta o titulo da janela
window.geometry('450x300') #seta o tamanho da janela

#cria uma entrada de texto centralizada na janela
entry = Entry(window, width = 25, justify='center') 
entry.insert(0, 'Digite o ID do Facebook') #seta o texto
entry.pack() #gerenciador de geometria
entry.focus_set() #obtém o foco para a entrada de texto
old_label_image = None

#função para evento de click do botão
def handleClick():
  global old_label_image
  ID = entry.get() #obtém o texto
  if not ID: #se texto vazio
    entry.insert(0, 'Digite o ID do Facebook')
  else:
    #encontrou a imagem no profile
    if getPhoto(ID):
      #carrega a imagem
      img = ImageTk.PhotoImage(Image.open(ID + '.png'))
      #criando um label para inserir a imagem
      label_image = Label(window, image=img)
      label_image.image = img
      label_image.pack()
      if old_label_image is not None:
        old_label_image.destroy()
      old_label_image = label_image

    else:
      pass

#cria um botão
btn = Button(window, text='Show photo', width = 20, command=handleClick)
btn.pack()

#loop principal da aplicação
window.mainloop()