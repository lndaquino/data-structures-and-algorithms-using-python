import urllib.request

# response = urllib.request.urlopen('https://google.com')
response = urllib.request.urlopen('https://gist.github.com/marcoscastro')
info = response.read()
# print(info) #tipo byte
html = info.decode('UTF-8')
target = '<span class="f6 text-gray">'
position = 0

while True:
  posTarget = html.find(target, position)
  if posTarget == -1:
    break
  
  posTitle = posTarget + len(target)
  posTargetEnd = html.find('</span>', posTitle)
  title = html[posTitle : posTargetEnd].replace('\n', '').lstrip()
  position = posTargetEnd
  print(title)


