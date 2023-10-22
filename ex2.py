from searchPlus import *
from MedoTotal import *
from collections import deque
import time

def depth_first_tree_search_all_count(problem, optimal=False, verbose=False):
    initTime = time.time()

    if not problem:
        return None

    stack = deque()
    visited = set()
    n1 = Node(problem.initial)
    stack.append(n1)
    visited.add(n1.state)
    max_mem = 0
    estados_finais = []
    beststate = None

    while(stack):
        t = time.time()
        if t - initTime >= 5.7:
            print("time: ",t-initTime)
            print("max_mem: ", max_mem)
            print("visitados: ", len(visited))
            print("estados finais: ", len(estados_finais))
            return


        node = stack.pop()
        state = node.state
        if len(stack) > max_mem:
            max_mem = len(stack)
            
        if optimal:
            if beststate is not None and node.path_cost >= beststate.path_cost:
                continue
            if verbose:
                print("---------------------")
                print()
                print(problem.display(state))
            if problem.goal_test(state):
                if beststate is None or node.path_cost < beststate.path_cost:
                    estados_finais.append(node)
                    beststate = node
                    visited.add(state)
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
            visited.add(state)

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
            visited.add(state)
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
                    stack.insert(i, child) 
            continue
        


            # normal
        visited.add(state)
        if problem.goal_test(state):
            estados_finais.append(node)
            if beststate is None or node.path_cost < beststate.path_cost:
                beststate = node
            continue

        acts = problem.actions(state)
        l = len(acts)
        for i in range(l):
            lmi = l - i - 1
            action = acts[lmi]
            res = problem.result(state, action)
            child = Node(res, node, action, problem.path_cost(node.path_cost, state, action, res))
            stack.append(child) 
            visited.add(res)

        visited.add(state)

    return beststate, max_mem, len(visited), len(estados_finais)

def teste():
    parametros="T=15\nM=6\nP=10"
    linha1= "= = = = = =\n"
    linha2= "= * F @ * =\n"
    linha3= "= . . . . =\n"
    linha4= "= . = . . =\n"
    linha5= "= . = . . =\n"
    linha6= "= = = = = =\n"
    grelha=linha1+linha2+linha3+linha4+linha5+linha6
    mundoStandard2=parametros + "\n" + grelha
    gx=MedoTotal(mundoStandard2)
    resultado,max_mem,visitados,finais = depth_first_tree_search_all_count(gx)
    print('*'*20)
    if resultado:
        print("Solução Prof-total (árvore) com custo " + str(resultado.path_cost)+":")
        print(resultado.solution())
    else:
        print('\nSem Solução')
    print('Visitados=',visitados)
    print('Dimensão máxima da memória',max_mem)
    print('Estados finais:',finais)


    # while stack:
    #     node = stack.popleft()
    #     state = node.state
    #     if len(stack) > max_mem:
    #         max_mem = len(stack)
    #     if optimal and beststate is not None and node.path_cost >= beststate.path_cost:
    #         continue
    #     if verbose:
    #         print("---------------------")
    #         print()
    #         print(problem.display(state))
    
    #     if problem.goal_test(state):
    #         estados_finais.append(node)
    #         if beststate is None or node.path_cost < beststate.path_cost:
    #             beststate = node
    #             if verbose:
    #                 print("GGGGooooooallllll --------- com o custo:" ,node.path_cost)
    #                 print("Di best goal até agora")
    #                 visited.add(state)
    #                 continue
    #         visited.add(state)
    #         if verbose:
    #             if node in estados_finais:
    #                 print("GGGGooooooallllll --------- com o custo:" ,node.path_cost)
    #             else:
    #                 print("Custo:", node.path_cost)
    #         continue
    #     if verbose:
    #         print("Custo:", node.path_cost)
        
    #     for i, action in enumerate(problem.actions(state)):
    #         child = Node(problem.result(state, action), node, action, problem.path_cost(node.path_cost, state, action, problem.result(state, action)))
    #         if optimal:
    #             if (beststate is not None and child.path_cost >= beststate.path_cost) or (beststate is not None and node.path_cost >= beststate.path_cost):
    #                 continue
    #         stack.insert(i, child)

    #     visited.add(state)
            