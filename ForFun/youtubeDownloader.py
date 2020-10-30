from tkinter import *
from youtubePytube import *

window = Tk()
window.title('Youtube Downloader')
window.geometry('500x200')
window.resizable(0, 0)

title = Label(window, text='Youtube Downloader', font=('Arial', 25), fg = 'Blue')
title.pack()

msg = Label(window, text='', font=('Arial', 15))

entry_url = Entry(window, width = 60, justify = 'center')
entry_url.insert(0, 'Enter url')
entry_url.pack()
entry_url.focus_set()

entry_name_video = Entry(window, width = 60, justify = 'center')
entry_name_video.insert(0, 'Enter video name')
entry_name_video.pack()

#função para evento de clique no botão
def handleClick():
  #obtém os textos
  url = entry_url.get()
  name_video = entry_name_video.get()

  if download_video(url, name_video):
    msg['fg'] = 'Green'
    msg['text'] = 'Download feito com sucesso!'
  else:
    msg['fg'] = 'Red'
    msg['text'] = 'Falha no download... :('

btn = Button(window, text = 'Download now', width = 20, command = handleClick)
btn.pack()

msg.pack()

window.mainloop()