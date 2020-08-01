import pygame
import sys

class Event(object):
    def Quit(self):
        if pygame.event.get(pygame.QUIT):
            sys.exit(0)
    def MouseButtonDown(self):
        return pygame.event.get(pygame.MOUSEBUTTONDOWN)

class Sprite(object):
    def __init__(self,src,width,height,pos,level=0):
        self.image=pygame.image.load(src)
        self.width=width
        self.height=height
        self.rect=pygame.transform.scale(self.image,(self.width,self.height))
        self.pos=pos
        self.level=level
    def scale(self,width,height):
        self.width=width
        self.height=height
        self.rect=pygame.transform.scale(self.image,(self.width,self.height))