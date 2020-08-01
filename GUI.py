#import pyQt5 as qt
from engine import *

BUTTON=0
FONT=1

class Font(object):
    def __init__(self,content,pos,font_size,font_type='assets/Deng.ttf',font_color=(0,0,0)):
        self.font_surf=pygame.font.Font(font_type,font_size).render(content,1,font_color)
        self.font_pos=pos
        self.ui_type=FONT
        self.__font_type=font_type
        self.__font_size=font_size
        self.__font_clr=font_color
    def set_content(self,content):
        self.font_surf=pygame.font.Font(self.__font_type,self.__font_size).render(content,1,self.__font_clr)

class Button(object):
    def __init__(self,width,height,pos,event_handler,fonts='',font_size=50,font_type='Arial',font_color=(0,0,0),src='assets/default/button.png'):
        self.sprite=Sprite(src,width,height,pos)
        self.font=Font(fonts,(0,0),font_size,font_type,font_color)
        fontposx=self.sprite.pos[0]+self.sprite.width/2 -self.font.font_surf.get_width()/2
        fontposy=self.sprite.pos[1] + self.sprite.height/2-self.font.font_surf.get_height()/2
        self.font.font_pos=(fontposx,fontposy)
        self.button_clicked=event_handler
        self.ui_type=BUTTON
    def clicked(self,pos)->bool:
        return pos[0]>=self.sprite.pos[0] and pos[0]<=self.sprite.pos[0]+self.sprite.width \
               and pos[1]>=self.sprite.pos[1] and pos[1]<=self.sprite.pos[1]+self.sprite.height