import MedoTotal
from searchPlus import *
from MedoTotal import *

class MedoTotalTurbo(MedoTotal):

    def __init__(self, texto_input):
        # Call the constructor of the superclass (MedoTotal) to initialize attributes
        super().__init__(texto_input)
        self.distPast = {} #p = pastilha xy[][] = matriz com a distância de cada (x,y) a p
        ps = self.initial[1]
        for i in range(len(ps)):
            self.distPast[ps[i]] = self.distanciasP(self, ps[i])

    def distanciasP(self, p):
        d = self.dim
        dists = [d][d]

        walkable = [d][d]
        for y in range(d):
            for x in range(d):
                if (x,y) in self.obstaculos or (x,y) == self.fantasma:
                    walkable[y][x] = False
                else:
                    walkable[y][x] = True

        for y in range(d):
            for x in range(d):
                dists[y][x] = self.distP(self, p, (x,y))

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
            
            # moving up
            if self.isValid(self, src[0] - 1, src[1], visited):
                queue.append((src[0] - 1, src[1], src[2] + 1))
                visited.append(src[0] + 1,src[1])
 
            # moving down
            if self.isValid(self, src[0] + 1, src[1], visited):
                queue.append((src[0] + 1, src[1], src[2] + 1))
                visited.append(src[0] + 1,src[1])
 
            # moving left
            if self.isValid(self, src[0], src[1] - 1, visited):
                queue.append((src[0], src[1] - 1, src[2] + 1))
                visited.append(src[0],src[1] - 1)
    
            # moving right
            if self.isValid(self, src[0], src[1] + 1, visited):
                queue.append((src[0], src[1] + 1, src[2] + 1))
                visited.append(src[0],src[1] + 1)
 
        return -1
 
 
    #checking where move is valid or not
    def isValid(self, x, y, visited):
        if ((x >= 0 and y >= 0) and
            ((x < self.dim) and
            y < self.dim) and
            ((x,y) not in self.obstaculos) and
            ((x,y) != self.fantasma) and
            ((x,y) not in visited)):

            return True
        return False