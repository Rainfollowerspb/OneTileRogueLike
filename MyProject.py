import pygame
import Layout as L
import Variables as V

pygame.init()

gameRunning = True

screen = pygame.display.set_mode((800, 600))
tempCoords = V.coords
tempRect = screen.get_rect()
# background = L.makeNewSurface(screen.get_size(), (192,192,192)),

paramsList = [
    # ["surfaceName", (width, height), (absX, absY, relX, relY), (Red. Green, Blue)], -- relX, relY = 0 if you want absolute positioning
    ["background", screen.get_size(), (0,0,0,0), (128,128,128)],
    ["bgSurface", L.scaleDown(screen.get_size(), V.globalMargin), (V.globalMargin,V.globalMargin,0,0), (192,192,192)],
    ["tunnelUp", (64,64), (2*V.globalMargin, 2*V.globalMargin, 0, 0), (96,96,128)],
    ["tunnelMid", (64,64), (2*V.globalMargin, 2*V.globalMargin, 0, V.globalMargin), (96,96,128)],
    ["tunnelDn", (64,64), (2*V.globalMargin, 2*V.globalMargin, 0, V.globalMargin), (96,96,128)],
    ["charPanel", (128, 256), (V.globalMargin, 2*V.globalMargin, 2*V.globalMargin, 0), (128, 96, 96)],
    ["distanceBar_1", (78, 32), (0, 2*V.globalMargin, 2*V.globalMargin, 0), (155, 155, 96)],
    ["distanceBar_2", (78, 32), (0, 2*V.globalMargin, 2, 0), (155, 155, 96)],
    ["distanceBar_3", (78, 32), (0, 2*V.globalMargin, 2, 0), (155, 155, 96)],
    ["distanceBar_4", (78, 32), (0, 2*V.globalMargin, 2, 0), (155, 155, 96)],
    ["distanceBar_5", (78, 32), (0, 2*V.globalMargin, 2, 0), (155, 155, 96)],
    # ["name", (dimensions), (margin), (color)],
]

objectDict = {}
coordsDict = {}

for i in range(len(paramsList)):
    tempSurface = L.makeNewSurface(paramsList[i][1], paramsList[i][3])
    objectDict[paramsList[i][0]] = tempSurface
    tempCoords = L.makePositioning(tempCoords, paramsList[i][2], tempRect)
    coordsDict[paramsList[i][0]] = tempCoords
    tempRect = tempSurface.get_rect()
    screen.blit(tempSurface,tempCoords)

# ---------------------
pygame.display.flip()

while gameRunning:
    # milliseconds = clock.tick(FPS)
    # playtime += milliseconds / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameRunning = False

    # pygame.display.flip()