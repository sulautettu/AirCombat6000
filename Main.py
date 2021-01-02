import pygame
import Player
import Server
import queue

controlDataToPyGame = queue.Queue()
controlDict = {}

Server.initServer(controlDataToPyGame)


pygame.init()
screen = pygame.display.set_mode((1920,1000))

#backround
backround = pygame.image.load('images/tausta.png')

#Caption and icon
pygame.display.set_caption("AirCombat6000")
icon = pygame.image.load('images/caption_icon.png')
pygame.display.set_icon(icon)


running = True

playerList = []
playerList.append(Player.player())
playerList.append(Player.player('Goose',1800,100))
playerList.append(Player.player('ice',600,100))

for player in playerList:
    print(player.name)

def drawPlayer():

    for player in playerList:
        image = pygame.image.load(player.imagePath)
        rotatedImage = pygame.transform.rotate(image, player.pitch)
        screen.blit(rotatedImage,(player.x,player.y))

        #print(player.x, player.y)


def updatePlayer():
    global controlDataToPyGame

    for player in playerList:
        player.update()

    #if controlDataToPyGame.empty():
        #print("empty")
      # pass
   #else:
      #  controlWord = controlDataToPyGame.get()
      #  print(type(controlWord["y"]))
       # playerList[1].pitchRate = int(controlWord["y"])/20



def checkServer():
    while not controlDataToPyGame.empty():
        controlWord = controlDataToPyGame.get()
        print("checkServer")
        for player in playerList:
            if player.name == controlWord["name"]:
                player.pitchRate = int(controlWord["y"])/50



while running:

    #backround image
    screen.blit(backround, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerList[1].pitchRate += 1
            if event.key == pygame.K_DOWN:
                playerList[1].pitchRate -= 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerList[1].pitchRate = 0

    updatePlayer()
    drawPlayer()
    checkServer()
    pygame.display.update()