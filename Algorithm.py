import random
import queue

class Atar:
    def __init__(self):
        self.g=[[0 for i in range(20)] for j in range(20)]
        self.back=[[(-1,-1) for i in range(20)] for j in range(20)]
        self.F=[[0 for i in range(20)] for j in range(20)]
        self.G=[[0 for i in range(20)] for j in range(20)]
        self.start=(-1,-1)
        self.end=(-1,-1)
        self.qu=queue.PriorityQueue()
        self.running=False
        self.mx=[-1,1,0,0]
        self.my=[0,0,-1,1]
        self.f=0
    def dist(self,p,q):
        return abs(p[0]-q[0])+abs(p[1]-q[1])
    def in_range(self,pos):
        return pos[0]>=0 and pos[0]<20 and pos[1]>=0 and pos[1]<20
    def clear(self):
        self.g = [[0 for i in range(20)] for j in range(20)]
        self.back = [[(-1, -1) for i in range(20)] for j in range(20)]
        self.start = (-1, -1)
        self.end = (-1, -1)
        self.running=False
        self.f=0
    def genedata(self):
        self.running=False
        self.f=0
        self.back = [[(-1, -1) for i in range(20)] for j in range(20)]
        self.start=(random.randint(0,9),random.randint(0,9))
        self.end=((random.randint(10,19),random.randint(10,19)))
        self.g[self.start[0]][self.start[1]]=-2
        self.g[self.end[0]][self.end[1]]=-3
        for i in range(20):
            for j in range(20):
                if (i,j)!=self.start and (i,j)!=self.end:
                    self.g[i][j]=-1 if random.randint(0,100)<34 else 0
                self.F[i][j]=self.dist(self.end,(i,j))
                self.G[i][j]=self.dist(self.start,(i,j))
    def restart(self):
        while not self.qu.empty():
            self.qu.get()
        self.qu.put((self.F[self.start[0]][self.start[1]],self.start))
        self.back = [[(-1, -1) for i in range(20)] for j in range(20)]
        for i in range(20):
            for j in range(20):
                self.g[i][j]=min(self.g[i][j],0)
        self.running=True
        self.f=0
    def next(self)->bool:
        if not self.running:
            return False
        if self.qu.empty():
            self.running=False
            return True
        cur=self.qu.get()
        self.f=cur[0]
        cur=cur[1]
        if cur!=self.start:
            self.g[cur[0]][cur[1]]=2
        for i in range(4):
            nxt=(cur[0]+self.mx[i],cur[1]+self.my[i])
            if self.in_range(nxt):
                if self.g[nxt[0]][nxt[1]]==0:
                    self.g[nxt[0]][nxt[1]]=1
                    self.back[nxt[0]][nxt[1]]=cur
                    self.qu.put((self.F[nxt[0]][nxt[1]],nxt))
                elif self.g[nxt[0]][nxt[1]]==1:
                    bk=self.back[nxt[0]][nxt[1]]
                    if self.G[bk[0]][bk[1]]>self.G[cur[0]][cur[1]]:
                        self.back[nxt[0]][nxt[1]]=cur
                elif nxt==self.end:
                    self.back[nxt[0]][nxt[1]]=cur
                    while cur!=self.start:
                        self.g[cur[0]][cur[1]]=3
                        cur=self.back[cur[0]][cur[1]]
                    self.running=False
        return True