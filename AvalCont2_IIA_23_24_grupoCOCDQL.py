from searchPlus import *
from MedoTotal import *
from collections import namedtuple
from collections import deque
from GrafoAbstracto import *

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
    

#------------------------------------------------------------------------------------------------------------

    
def depth_first_tree_search_all_count(problem, optimal=False, verbose=False):

    if not problem:
        return None

    stack = deque()
    visited = list()
    n1 = Node(problem.initial)

    stack.append(n1)
    if not optimal:
        visited.append(n1)
    
    max_mem = 0
    estados_finais = []
    beststate = None

    while(stack):
            
        node = stack.pop()
        state = node.state
        npc = node.path_cost
 
        if optimal:
            if verbose:
                print("---------------------")
                print()
                print(problem.display(state))
                print("Custo:", node.path_cost)

            acts = problem.actions(state)
            l = len(acts)
            for i in range(len(acts)):
                lmi = l - i - 1
                action = acts[lmi]
                res = problem.result(state, action)
                
                if problem.goal_test(res):

                    a2 = acts[i]
                    res2 = problem.result(state, a2)
                    child = Node(res2, node, a2, problem.path_cost(npc, state, a2, res2))

                    if beststate is not None and child.path_cost >= beststate.path_cost:
                        continue
                    
                    estados_finais.append(child)
                    if verbose:
                        print("---------------------")
                        print()
                        print(problem.display(res2))

                    if beststate is None or child.path_cost < beststate.path_cost:
                        beststate = child
                        if verbose:
                            print("GGGGooooooallllll --------- com o custo:" ,child.path_cost)
                            print("Di best goal até agora")
                    else:
                        if verbose:
                            if child in estados_finais:
                                print("GGGGooooooallllll --------- com o custo:" ,child.path_cost)
                            else:
                                print("Custo:", child.path_cost)
                    visited.append(child)
                else:
                    child = Node(res, node, action, problem.path_cost(node.path_cost, state, action, res))
                    if beststate is None or child.path_cost < beststate.path_cost:
                        stack.append(child)
            visited.append(node)

            ls = len(stack)
            if ls > max_mem:
                max_mem = ls
            continue  

        if verbose:
            print("---------------------")
            print()
            print(problem.display(state))
            print("Custo:", node.path_cost)
            
            acts = problem.actions(state)
            l = len(acts)
            for i in range(l):
                action = acts[l - i - 1]
                res = problem.result(state, action)
                
                if problem.goal_test(res):
                    a2 = acts[i]
                    res2 = problem.result(state, a2)
                    child = Node(res2, node, a2, problem.path_cost(npc, state, a2, res2))

                    estados_finais.append(child)
                    print("---------------------")
                    print()
                    print(problem.display(res2))
                    if beststate is None or child.path_cost < beststate.path_cost:
                        beststate = child
                        print("GGGGooooooallllll --------- com o custo:" ,child.path_cost)
                        print("Di best goal até agora")
                    else:
                        if child in estados_finais:
                            print("GGGGooooooallllll --------- com o custo:" ,child.path_cost)
                        else:
                            print("Custo:", child.path_cost)
                    
                else:
                    child = Node(res, node, action, problem.path_cost(npc, state, action, res))
                    stack.append(child) 
                visited.append(child)
            ls = len(stack)
            if ls > max_mem:
                max_mem = ls
            continue

        acts = problem.actions(state)
        l = len(acts)
        for i in range(l):
            lmi = l - i - 1
            action = acts[lmi]
            npc = node.path_cost
            res = problem.result(state, action)
            child = Node(res, node, action, problem.path_cost(npc, state, action, res))
            
            if problem.goal_test(res):
                estados_finais.append(child)
                
                if beststate is None or child.path_cost < beststate.path_cost:
                    beststate = child
                visited.append(child)
            else:
                visited.append(child)
                stack.append(child) 
        ls = len(stack)
        if ls > max_mem:
            max_mem = ls
    return beststate, max_mem, len(visited), len(estados_finais)


#------------------------------------------------------------------------------------------------------------


def ida_star_graph_search_count(problem,f,verbose=False):
    if not problem:
        return None
    
    initialState = problem.initial
    fronteira = deque()

    lastNode = None

    initialNode = Node(initialState, None, None, 0)

    fronteira.append(initialNode)
    beenThereDoneThat = set()
    beenThereDoneThat.add(initialState)

    size = 1

    cutoff = f(initialNode)
    miniCut = infinity

    if verbose:
        print("------Cutoff at", cutoff)

    i = 0

    while fronteira:

        node = fronteira.pop()

        predict = f(node)

        if verbose:
            print("\n" + node.state)
            print("Cost:", node.path_cost, "f=", predict)

        if predict > cutoff:
            miniCut = min(predict, miniCut)
            if verbose:
                print("Out of cutoff -- minimum out:", miniCut)
        else:

            if problem.goal_test(node.state):
                lastNode = node
                if verbose:
                    print("Goal found within cutoff!")
                break

            frontExtension = node.expand(problem)
            frontExtension.reverse()

            for n in frontExtension:
                if n.state not in beenThereDoneThat:

                    fronteira.append(n)
                    size += 1
                    beenThereDoneThat.add(n.state)

        i += 1

        if not fronteira and miniCut != infinity:
            fronteira.append(initialNode)

            beenThereDoneThat.clear()
            beenThereDoneThat.add(initialState)
            size += 1

            cutoff = miniCut
            miniCut = infinity

            if verbose:
                print("\n\n------Cutoff at", cutoff)

    return lastNode, size