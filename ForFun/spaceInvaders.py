#task - nave não sair dos limites da tela, tempo acaba mostra resultado e encerra, pode atirar vários mísseis, inimigos tb atirarem, inimigos fazerem movimentos laterais, inimigos não aparecerem sobrepostos, criar db pra armazenar melhores pontuações, usuário pode iniciar jogo e definir nome
import pygame, random, schedule

white = (255,255,255)
red = (255, 0, 0)

#inicializa e configura janela
pygame.init()
width, height = 800, 600
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Space Invaders')

#inicializa nave
imgNave = pygame.image.load('nave.png')
posNave = [350,520]

#inicializa míssel
imgMissile = pygame.image.load('missile.png')
posMissile = [None, None]
flagMissile = False

#inicializa inimigos
enemies, countEnemies = [], 5
for i in range(countEnemies):
  posX, posY = random.randint(10, width - 10), -10
  enemy = [pygame.image.load('enemy.png'), posX, posY]
  enemies.append(enemy)

def updateEnemies():
   #atualiza posição dos inimigos
  for i in range(countEnemies):
    #inimigo vai descendo a tela
    enemies[i][2] += 1
    #se inimigo sair da tela
    if enemies[i][2] > (height + 10):
      #gera nova posição e retorna para topo da tela
      posX = random.randint(10, width - 10)
      enemies[i][1], enemies[i][2] = posX, -10

def updateMissile():
  global flagMissile
  if flagMissile:
    #verifica se passou dos limites da tela
    if posMissile[1] < -imgMissile.get_rect().size[1]:
      flagMissile = False
    else:
      posMissile[1] -= 5

def updateRemainingTime():
  global timeRemaining, timeRemainingText
  if timeRemaining > 0:
    timeRemaining -= 1
    timeRemainingText = font.render('Tempo: ' + str(timeRemaining), 1, red)


schedule.every(0.01).seconds.do(updateEnemies)
schedule.every(0.01).seconds.do(updateMissile)
schedule.every(1).seconds.do(updateRemainingTime)

#pontuação do jogo
score = 0
font = pygame.font.Font(None, 30)
scoreText = font.render('Score: ' +  str(score), 1, red)

#tempo restante
timeRemaining = 60
fontTime = pygame.font.Font(None, 30)
timeRemainingText = fontTime.render('Tempo: ' + str(timeRemaining), 1, red)


def updateScore(decrement = False):
  global score, scoreText
  if timeRemaining > 0:
    score = (score - 1) if decrement else (score + 1)
    scoreText = font.render('Score: ' + str(score), 1, red)

def resetEnemy(index):
  enemies[index][1] = random.randint(10, width - 10)
  enemies[index][2] = -10

mainLoop = True

while mainLoop:
  #busca eventos
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      mainLoop = False
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
      flagMissile = True

  #obtém a tecla pressionada para mudar posição da nave
  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_LEFT]:
    posNave[0] -= 1
  elif pressed[pygame.K_RIGHT]:
    posNave[0] += 1
  elif pressed[pygame.K_UP]:
    posNave[1] -= 1
  elif pressed[pygame.K_DOWN]:
    posNave[1] += 1

  window.fill(white)
  
  schedule.run_pending()

  if not flagMissile:
    posMissile = [posNave[0], posNave[1]]

  missile = window.blit(imgMissile, posMissile)
  nave = window.blit(imgNave, posNave)
  for i in range(countEnemies):
    enemy = window.blit(enemies[i][0], (enemies[i][1], enemies[i][2]))
    #verifica colisão dos inimigos com a nave
    if nave.collidepoint((enemies[i][1], enemies[i][2])):
      resetEnemy(i)
      updateScore(decrement = True)
    #verifica colisão do missel com os inimigos
    if missile.collidepoint((enemies[i][1], enemies[i][2])):
      resetEnemy(i)
      updateScore() #incrementa score
      flagMissile = False

  window.blit(scoreText, (10, 10))
  window.blit(timeRemainingText, (680, 10))

  pygame.display.flip()


pygame.quit()
print('Fim de jogo')