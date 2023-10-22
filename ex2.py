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
            if beststate is not None and node.path_cost >= beststate.path_cost:
                continue
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
