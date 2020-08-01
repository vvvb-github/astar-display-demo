import pygame
import sys
import os
import GUI as ui

class Game(object):
    def __init__(self,window_width,window_height,title):
        pygame.init()
        os.environ['SDL_VIDEO_WINDOW_POS']='%d,%d'%(500,50)
        pygame.font.init()
        size=window_width,window_height
        self.screen=pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.clock=pygame.time.Clock()
        self.sprite_pool=list()
        self.ui_pool=list()
        self.static_sprite_pool=list()
        self.static_ui_pool=list()
    def Render(self):
        self.screen.fill((125,125,125))
        for sprite in self.static_sprite_pool:
            self.screen.blit(sprite.rect, sprite.pos)
        for sprite in self.sprite_pool:
            self.screen.blit(sprite.rect,sprite.pos)
        for ui_controller in self.ui_pool:
            if ui_controller.ui_type==ui.BUTTON:
                self.screen.blit(ui_controller.sprite.rect,ui_controller.sprite.pos)
                self.screen.blit(ui_controller.font.font_surf,ui_controller.font.font_pos)
            elif ui_controller.ui_type==ui.FONT:
                self.screen.blit(ui_controller.font_surf,ui_controller.font_pos)
        for ui_controller in self.static_ui_pool:
            if ui_controller.ui_type==ui.BUTTON:
                self.screen.blit(ui_controller.sprite.rect,ui_controller.sprite.pos)
                self.screen.blit(ui_controller.font.font_surf,ui_controller.font.font_pos)
            elif ui_controller.ui_type==ui.FONT:
                self.screen.blit(ui_controller.font_surf,ui_controller.font_pos)
        pygame.display.flip()
    def Line(self,p,q,color):
        pygame.draw.aaline(self.screen,color,p,q,1)
    def Event_Handle(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit(0)
            elif event.type==pygame.MOUSEBUTTONDOWN:
                for ui_controller in self.ui_pool:
                    if ui_controller.ui_type==ui.BUTTON and ui_controller.clicked(event.pos):
                        ui_controller.button_clicked()
                for ui_controller in self.static_ui_pool:
                    if ui_controller.ui_type==ui.BUTTON and ui_controller.clicked(event.pos):
                        ui_controller.button_clicked()