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
        


            
        if optimal:
            if beststate is not None and node.path_cost >= beststate.path_cost:
                continue
            if verbose:
                print("---------------------")
                print()
                print(problem.display(state))
                
                
                
                
            # if problem.goal_test(state):
            #     if beststate is None or node.path_cost < beststate.path_cost:
            #         estados_finais.append(node)
            #         beststate = node
            #         visited.append(node)
            #         if verbose:
            #             print("GGGGooooooallllll --------- com o custo:" ,node.path_cost)
            #             print("Di best goal até agora")
            #     else:
            #         if verbose:
            #             if node in estados_finais:
            #                 print("GGGGooooooallllll --------- com o custo:" ,node.path_cost)
            #             else:
            #                 print("Custo:", node.path_cost)
            #     continue
            # else:
            #     if verbose:
            #         print("Custo:", node.path_cost)
            #     if beststate is not None and node.path_cost >= beststate.path_cost:
            #         continue





            acts = problem.actions(state)
            l = len(acts)
            for i in range(len(acts)):
                lmi = l - i - 1
                action = acts[lmi]
                res = problem.result(state, action)
                child = Node(res, node, action, problem.path_cost(node.path_cost, state, action, res))
                if (beststate is not None and child.path_cost >= beststate.path_cost):
                    continue
                
                if problem.goal_test(res):
                    estados_finais.append(child)
                    if beststate is None or child.path_cost < beststate.path_cost:
                        beststate = child
                        visited.append(child)
                        if verbose:
                            print("GGGGooooooallllll --------- com o custo:" ,child.path_cost)
                            print("Di best goal até agora")
                    else:
                        if verbose:
                            if child in estados_finais:
                                print("GGGGooooooallllll --------- com o custo:" ,child.path_cost)
                            else:
                                print("Custo:", child.path_cost)
                    continue
                
                
                
                stack.append(child)
                
                
                
            visited.append(node)
            continue  
            
            
            
            
            
            
        if verbose:
            
            
            print("---------------------")
            print()
            print(problem.display(state))
            print("Custo:", node.path_cost)
            
            
            
            
            
            
            acts = problem.actions(state)
            l = len(acts)
            for i in range(l):
                action = acts[i]
                npc = node.path_cost
                res = problem.result(state, action)

                child = Node(res, node, action, problem.path_cost(npc, state, action, res))
                
                if problem.goal_test(res):
                    estados_finais.append(child)
                    print("---------------------")
                    print()
                    print(problem.display(res))
                    if beststate is None or child.path_cost < beststate.path_cost:
                        beststate = child
                        print("GGGGooooooallllll --------- com o custo:" ,child.path_cost)
                        print("Di best goal até agora")
                    # else:
                    #     if child in estados_finais:
                    #         print("GGGGooooooallllll --------- com o custo:" ,child.path_cost)
                    #     else:
                    #         print("Custo:", child.path_cost)
                    visited.append(child)
                else:
                    # print("---------------------")
                    # print()
                    # print(problem.display(res))
                    # print("Custo:", child.path_cost)
                    visited.append(child)
                    stack.append(child) 
            ls = len(stack)
            if ls > max_mem:
                max_mem = ls
            continue
        





    
        # npc = node.path_cost
        # if problem.goal_test(state):
        #     estados_finais.append(node)
        #     if beststate is None or npc < beststate.path_cost:
        #         beststate = node
        #     continue

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






def  teste():
	
    parametros="T=6\nM=4\nP=10"
    linha1= "= = = = = =\n"
    linha2= "= . @ F * =\n"
    linha3= "= . . . . =\n"
    linha4= "= . = . . =\n"
    linha5= "= . = . . =\n"
    linha6= "= = = = = =\n"
    grelha=linha1+linha2+linha3+linha4+linha5+linha6
    mundoStandardx=parametros + "\n" + grelha
    gx=MedoTotal(mundoStandardx)

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