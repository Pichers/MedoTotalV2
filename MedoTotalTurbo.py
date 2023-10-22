from searchPlus import *
from MedoTotal import *
from collections import namedtuple

class MedoTotalTurbo(MedoTotal):

    def __init__(self, texto_input):
        super().__init__(texto_input)
        self.distPast = {}
        ps = self.initial[1]
        for p in ps:
            self.distPast[p] = self.distanciasP(p)

    def distanciasP(self, p):
        d = self.dim

        dists = [[None for _ in range(d)] for _ in range(d)]
        walkable = [[None for _ in range(d)] for _ in range(d)]

        for y in range(d):
            for x in range(d):
                if (x,y) in self.obstacles or (x,y) == self.fantasma:
                    walkable[y][x] = False
                else:
                    walkable[y][x] = True

        for y in range(d):
            for x in range(d):
                if not walkable[y][x]:
                    dists[y][x] = None
                else:
                    dists[y][x] = self.distP(p, (x,y))
        return dists
        
    def distP(self, p, c):
        (x,y) = c
        src = (x, y, 0)

        visited = []
        visited.append(src)

        queue = []
        queue.append(src)

        while len(queue) != 0:

            src = queue.pop(0)

            if((src[0], src[1]) == p):
                return src[2]
            
            # moving left
            if self.isValid(src[0] - 1, src[1], visited):
                queue.append((src[0] - 1, src[1], src[2] + 1))
                visited.append((src[0] - 1, src[1]))
 
            # moving right
            if self.isValid(src[0] + 1, src[1], visited):
                queue.append((src[0] + 1, src[1], src[2] + 1))
                visited.append((src[0] + 1, src[1]))
 
            # moving up
            if self.isValid(src[0], src[1] - 1, visited):
                queue.append((src[0], src[1] - 1, src[2] + 1))
                visited.append((src[0], src[1] - 1))
    
            # moving down
            if self.isValid(src[0], src[1] + 1, visited):
                queue.append((src[0], src[1] + 1, src[2] + 1))
                visited.append((src[0], src[1] + 1))
 
        return -1
 
    def isValid(self, x, y, visited):
        if ((x >= 0 and y >= 0) and
            (x < self.dim and y < self.dim) and
            (x,y) not in self.obstacles and
            (x,y) != self.fantasma and
            (x,y) not in visited):

            return True
        return False
    
    def actions(self, state):
        x, y = state.pacman
        return [act for act in self.directions.keys() 
                if (x+self.directions[act][0],y+self.directions[act][1]) not in (self.obstacles | {self.fantasma}) and 
                not self.falha_antecipada(self.result(state,act))]
    
    def falha_antecipada(self,state):
        pacman = state[0]

        if state.tempo <= state.medo:
            return False
        if state.pastilhas == set():
            return True
        
        dists = []
        for p in state[1]:
            dists.append(self.distPast[p][pacman[1]][pacman[0]])
        minDist = min(dists)

        if minDist > state.medo:
            return True
        if (state.medo + self.poder * len(state.pastilhas)) < state.tempo:
            return True
        return False
