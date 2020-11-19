import pygame

margin = 25
screen = pygame.display.set_mode((800, 600))
coords = (0, 0)

def makeNewSurface(dimensions, color):
    tempSurface = pygame.Surface(dimensions)
    tempSurface.fill(color)
    tempSurface = tempSurface.convert()
    return tempSurface

def scaleDown(size, margin):
    width, height = size
    width -= 2* margin
    height -= 2* margin
    size = (width, height)
    return size

def makePositioning(coords, margin, rect):
    x, y, width, height = rect
    x, y = coords
    absX, absY, relX, relY = margin
    if relX:
        x = x + width + relX
    else:
        x = absX

    if relY:
        y = y + height + relY
    else:
        y = absY

    coords = x, y
    return coords

objectDict = [
    # ((width, height), (absX, absY), (relX, relY), (red, green, blue)),
]