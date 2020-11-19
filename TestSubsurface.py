# -*- coding: utf-8 -*-

import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
screenRect = screen.get_rect()

gamerunning = True

def makeSurface(baseSurface, width, height, x, y, color):
    tempSurface = pygame.Surface((width,height))
    tempSurface.fill(color)
    tempSurface = tempSurface.convert()
    baseSurface.blit(tempSurface, (x, y))
    return baseSurface

background = makeSurface(screen, screenRect.width, screenRect.height, 0, 0, (255,255,255))
foreground = makeSurface(background, 100, 100, 50, 50, (255,0,0))

# while gamerunning

pygame.display.flip()