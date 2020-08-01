from engine import *
from GUI import *

class Res(object):
    def __init__(self):
        self.sprite_res={
            'tool_bar':Sprite('assets/default/button.png',500,80,(50,10))
        }
        self.ui_res={
            'Start_btn':Button(100,50,(100,625),0,'开始',20,'assets/Deng.ttf'),
            'Gene_btn':Button(100,50,(400,625),0,'生成',20,'assets/Deng.ttf'),
            'F':Font('当前估价（曼哈顿距离）=0',(150,40),20)
        }