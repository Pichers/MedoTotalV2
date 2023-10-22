from searchPlus import *
from MedoTotal import *
from collections import deque
import time

def depth_first_tree_search_all_count(problem, optimal=False, verbose=False):

    if not problem:
        return None

    stack = deque()
    visited = list()
    n1 = Node(problem.initial)

    stack.append(n1)
    visited.append(n1)
    
    max_mem = 0
    estados_finais = []
    beststate = None

    while(stack):
    
        node = stack.pop()
        state = node.state
        
        ls = len(stack)
        if ls > max_mem:
            max_mem = ls
            
        if optimal:
            if verbose:
                print("---------------------")
                print()
                print(problem.display(state))
            if problem.goal_test(state):
                if beststate is None or node.path_cost < beststate.path_cost:
                    estados_finais.append(node)
                    beststate = node
                    visited.append(node)
                    if verbose:
                        print("GGGGooooooallllll --------- com o custo:" ,node.path_cost)
                        print("Di best goal até agora")
                else:
                    if verbose:
                        if node in estados_finais:
                            print("GGGGooooooallllll --------- com o custo:" ,node.path_cost)
                        else:
                            print("Custo:", node.path_cost)
                continue
            else:
                if verbose:
                    print("Custo:", node.path_cost)
                if beststate is not None and node.path_cost >= beststate.path_cost:
                    continue
            visited.append(node)

            acts = problem.actions(state)
            l = len(acts)
            for i in range(len(acts)):
                lmi = l - i - 1
                action = acts[lmi]

                res = problem.result(state, action)
                child = Node(res, node, action, problem.path_cost(node.path_cost, state, action, res))
                
                if(beststate is not None and child.path_cost >= beststate.path_cost):
                    continue
                stack.append(child)
            continue  
            
            
        if verbose:
            print("---------------------")
            print()
            print(problem.display(state))
            
            if problem.goal_test(state):
                estados_finais.append(node)
                if beststate is None or node.path_cost < beststate.path_cost:
                    beststate = node
                    print("GGGGooooooallllll --------- com o custo:" ,node.path_cost)
                    print("Di best goal até agora")
                else:
                    if node in estados_finais:
                        print("GGGGooooooallllll --------- com o custo:" ,node.path_cost)
                    else:
                        print("Custo:", node.path_cost)
                continue
            else:
                print("Custo:", node.path_cost)

                acts = problem.actions(state)
                l = len(acts)
                for i in range(len(acts)):
                    lmi = l - i - 1
                    action = acts[lmi]

                    res = problem.result(state, action)
                    child = Node(res, node, action, problem.path_cost(node.path_cost, state, action, res))

                    stack.append(child) 
                    visited.append(child)
            continue
        


            # normal
        npc = node.path_cost
        if problem.goal_test(state):
            estados_finais.append(node)
            if beststate is None or npc < beststate.path_cost:
                beststate = node
            continue

        acts = problem.actions(state)
        l = len(acts)
        for i in range(l):
            lmi = l - i - 1
            action = acts[lmi]

            res = problem.result(state, action)
            child = Node(res, node, action, problem.path_cost(npc, state, action, res))

            stack.append(child) 
            visited.append(child)

    return beststate, max_mem, len(visited), len(estados_finais)
