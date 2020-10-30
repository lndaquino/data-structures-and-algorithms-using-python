import urllib.request

def getPhoto(ID):
  try:
    url = 'https://graph.facebook.com/' + ID + '/picture?type=large'
    image = urllib.request.urlopen(url).read()
    file_name = ID + '.png'
    my_file = open(file_name, 'wb')
    my_file.write(image)
    my_file.close()
    return True
  
  except:
    return False