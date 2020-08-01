import Game
import Resources
import Algorithm
from engine import *
from GUI import *

def mp(pos,d=0)->tuple:
    return (50+pos[0]*25+d,100+pos[1]*25+d)

class App(object):
    def __init__(self):
        self.game=Game.Game(600,700,'A*')
        self.res=Resources.Res()
        self.astar=Algorithm.Atar()
        #bind event handler
        self.res.ui_res['Start_btn'].button_clicked=self.Start_clicked
        self.res.ui_res['Gene_btn'].button_clicked=self.Gene_clicked
        #load to pool
        self.game.static_ui_pool=[
            self.res.ui_res['Start_btn'],
            self.res.ui_res['Gene_btn'],
        ]
        self.game.static_sprite_pool = [
            self.res.sprite_res['tool_bar']
        ]
        self.res_upd()
    def exec(self,tick_flip):
        while True:
            self.game.clock.tick(tick_flip)
            self.game.Event_Handle()
            self.update()
    def update(self):
        if self.astar.next():
            self.res_upd()
    def res_upd(self):
        self.res.ui_res['F'].set_content('当前估价（曼哈顿距离）={0}'.format(self.astar.f))
        self.game.ui_pool=[
            self.res.ui_res['F']
        ]
        self.game.sprite_pool.clear()
        for i in range(20):
            for j in range(20):
                if self.astar.g[i][j] == 0:
                    self.game.sprite_pool.append(Sprite('assets/white.png', 25, 25, mp((i, j))))
                elif self.astar.g[i][j] == -1:
                    self.game.sprite_pool.append(Sprite('assets/black.png', 25, 25, mp((i, j))))
                elif self.astar.g[i][j] == -2:
                    self.game.sprite_pool.append(Sprite('assets/start.png', 25, 25, mp((i, j))))
                elif self.astar.g[i][j] == -3:
                    self.game.sprite_pool.append(Sprite('assets/end.png', 25, 25, mp((i, j))))
                elif self.astar.g[i][j] == 1:
                    self.game.sprite_pool.append(Sprite('assets/red.png', 25, 25, mp((i, j))))
                elif self.astar.g[i][j] == 2:
                    self.game.sprite_pool.append(Sprite('assets/green.png', 25, 25, mp((i, j))))
                else:
                    self.game.sprite_pool.append(Sprite('assets/yellow.png', 25, 25, mp((i, j))))
        self.game.Render()
    def Start_clicked(self):
        if self.astar.start!=(-1,-1):
            self.astar.restart()
    def Gene_clicked(self):
        self.astar.genedata()
        self.res_upd()