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
        

