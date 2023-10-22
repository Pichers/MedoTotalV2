from collections import deque
import time
from searchPlus import *
from MedoTotal import * 
from GrafoAbstracto import *


def ida_star_graph_search_count(problem,f,verbose=False):
    if not problem:
        return None
    
    initialState = problem.initial
    fronteira = deque()

    lastNode = None

    initialNode = Node(initialState, None, None, 0)

    fronteira.append(initialNode)
    beenThereDoneThat = list()
    beenThereDoneThat.append(initialNode)

    size = 1

    cutoff = f(initialNode)
    miniCut = infinity

    if verbose:
        print("------Cutoff at", cutoff)

    it = time.time()

    while fronteira:

        if(time.time() - it> 7):
            print("visitados", size)
            print("time:",time.time() - it)
            break

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

            for n in reversed(frontExtension):
                if n not in beenThereDoneThat:
                    fronteira.append(n)
                    size += 1
                    beenThereDoneThat.append(n)

        if not fronteira and miniCut != infinity:
            fronteira.append(initialNode)

            beenThereDoneThat = list()
            beenThereDoneThat.append(initialNode)
            size += 1

            cutoff = miniCut
            miniCut = infinity

            if verbose:
                print("\n\n------Cutoff at", cutoff)

    return lastNode, size
        

