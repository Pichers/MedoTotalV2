from searchPlus import *
from MedoTotal import *
from collections import namedtuple
import timeit

class MedoTotalTurbo(MedoTotal):

    def __init__(self, texto_input):
        # Call the constructor of the superclass (MedoTotal) to initialize attributes
        super().__init__(texto_input)
        self.distPast = {} #p = pastilha xy[][] = matriz com a distância de cada (x,y) a p
        ps = self.initial[1]
        for p in ps:
            self.distPast[p] = self.distanciasP(p)

    def distanciasP(self, p):
        d = self.dim

        # Initialize dists and walkable with empty lists
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
 
 
    #checking where move is valid or not
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
        if state.pastilhas == set(): # se não há mais pastilhas e eram necessárias
            return True
        
        #minDist = min(list(map(lambda x: manhatan(state.pacman,x),state.pastilhas)))
        dists = []
        for p in state[1]:
            dists.append(self.distPast[p][pacman[1]][pacman[0]])
        minDist = min(dists)

        if minDist > state.medo: # se não há tempo (manhatan) para chegar à próxima super-pastilha
            return True
        if (state.medo + self.poder * len(state.pastilhas)) < state.tempo:
            # se o poder de todas as pastilhas mais o medo são insuficientes.
            return True
        return False
    
#     #-------------------------------------------------------------------------

#     def depth_first_tree_search_all_count(self,problem,optimal=False,verbose=False):
        
#         if not problem:
#             return None

#         pilha = [] 
#         visited = set()
#         n1 = Node(problem.initial)
#         pilha.append(n1)
        
#         max_mem = 0
        
#         estados_finais = []
#         beststate = None

#         while(pilha):
#             if(len(pilha) > max_mem):
#                 max_mem = len(pilha)

#             n = pilha.pop(0)
#             state = n.state
            
#             if state not in visited:
#                 if verbose:
#                     print(problem.display(state))
#                     print("custo = ")
                    
#                 if optimal:
#                     if state.cost >= beststate.cost:
#                         continue

#                 visited.add(n)

#                 # for i in len(problem.actions(state)):
#                 for i in range(len(problem.actions(state))):
#                     action = problem.actions( state)[i]

#                     child = Node(problem.result(n, action))

#                     if problem.goal_test(child.state):
#                         estados_finais.append(child)
#                         if beststate == None or child.cost < beststate.cost:
#                             beststate = child
#                         continue
                    
#                     if child not in visited:
#                         pilha.insert(i,child)
        

        
#         #return ()
#         return beststate, max_mem, visited, estados_finais         
#     # resultado,max_mem,visitados,finais 
    
    



# # class teste:
    
# #     parametros="T=6\nM=4\nP=10"
# #     linha1= "= = = = = =\n"
# #     linha2= "= . @ F * =\n"
# #     linha3= "= . . . . =\n"
# #     linha4= "= . = . . =\n"
# #     linha5= "= . = . . =\n"
# #     linha6= "= = = = = =\n"
# #     grelha=linha1+linha2+linha3+linha4+linha5+linha6
# #     mundoStandard2=parametros + "\n" + grelha
# #     gx=MedoTotal(mundoStandard2)
# #     print(gx.display(gx.initial))
# #     start = timeit.default_timer()

# #     resultado,max_mem,visitados,finais = depth_first_tree_search_all_count(gx,verbose=True)

# #     stop = timeit.default_timer()
# #     print('*'*20)
# #     if resultado:
# #         print("\nSolução Prof-total (árvore) com custo", str(resultado.path_cost)+":")
# #         print(resultado.solution())
# #     else:
# #         print('\nSem Solução')
# #     print('Visitados=',visitados)
# #     print('Dimensão máxima da memória',max_mem)
# #     print('Estados finais:',finais)
# #     print('Time: ', stop - start)
