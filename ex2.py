from searchPlus import *
from MedoTotal import *
from collections import deque

def depth_first_tree_search_all_count(problem, optimal=False, verbose=False):
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

    while stack:
        node = stack.pop()
        state = node.state
        if len(stack) > max_mem:
            max_mem = len(stack)
            
        
        if optimal and beststate is not None and node.path_cost >= beststate.path_cost:
                continue
            
        if verbose:
            print("---------------------")
            print()
            print(problem.display(state))
            
        
        # if state not in visited: 

            
        if problem.goal_test(state):
            estados_finais.append(node)
            if beststate is None or node.path_cost < beststate.path_cost:
                beststate = node
                if verbose:
                    print("GGGGooooooallllll --------- com o custo:" ,node.path_cost)
                    print("Di best goal até agora")
                    visited.add(state)
                    continue
                    
                    
            visited.add(state)

            if verbose:
                if node in estados_finais:
                    print("GGGGooooooallllll --------- com o custo:" ,node.path_cost)
                else:
                    print("Custo:", node.path_cost)
            continue
        
        
        
        
        if verbose:
            print("Custo:", node.path_cost)
            
            
            
        for i, action in enumerate(problem.actions(state)):
            child_state = problem.result(state, action)
            child = Node(child_state, node, action, problem.path_cost(node.path_cost, state, action, child_state))
            if optimal:
                # if beststate is not None:
                #     print("child.path_cost:", child.path_cost, "beststate.path_cost:", beststate.path_cost)
                if beststate is not None and child.path_cost >= beststate.path_cost:
                    continue
            stack.insert(i, child)




        visited.add(state)
            

    return beststate, max_mem, len(visited), len(estados_finais)
