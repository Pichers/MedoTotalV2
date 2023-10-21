from searchPlus import *
from MedoTotal import *


def depth_first_tree_search_all_count(problem, optimal=False, verbose=False):
    if not problem:
        return None

    def recursive_search(pilha):

        node = pilha.pop(0)
        nonlocal max_mem, visited, estados_finais, beststate

        state = node.state

        if state not in visited:
            if verbose:
                print("---------------------")
                print()
                print(problem.display(state))
                print("Custo: ", node.path_cost)

            if problem.goal_test(state):
                estados_finais.append(node)
                if beststate is None or node.path_cost < beststate.path_cost:
                    beststate = node
                return

            for action in problem.actions(state):
                child_state = problem.result(state, action)
                child = Node(child_state, node, action, problem.path_cost(node.path_cost, state, action, child_state))

                if child.state not in visited:
                    if(optimal):
                        if(beststate != None and child.path_cost >= beststate.path_cost):
                            print("AAAAAAAAAAAA")
                            return
                    pilha.insert(0, child)
                    if len(pilha) > max_mem:
                        max_mem = len(pilha)
                    recursive_search(pilha)
            visited.add(state)
    pilha = []
    visited = set()
    n1 = Node(problem.initial)
    pilha.append(n1)

    max_mem = 0

    estados_finais = []
    beststate = None

    recursive_search(pilha)

    return beststate, max_mem, len(visited), len(estados_finais)


# def depth_first_tree_search_all_count(problem, optimal=False, verbose=False):
#     if not problem:
#         return None

#     pilha = []
#     visited = set()
#     n1 = Node(problem.initial)
#     pilha.append(n1)

#     max_mem = 0

#     estados_finais = []
#     beststate = None

#     while pilha:
#         if len(pilha) > max_mem:
#             max_mem = len(pilha)

#         n = pilha.pop(0)
#         state = n.state

#         if state not in visited:
#             if verbose:
#                 # print("---------------------")
#                 print()
#                 # print(problem.display(state))
#                 # print("Custo: ", n.path_cost)

#             visited.add(state)

#             if problem.goal_test(state):
#                 estados_finais.append(n)
#                 if beststate is None or n.path_cost < beststate.path_cost:
#                     beststate = n
#                 continue

#             for action in problem.actions(state):
#                 child_state = problem.result(state, action)
#                 child = Node(child_state, parent=n, action=action)

#                 if child not in visited:
#                     pilha.insert(0, child)
    
#     return beststate, max_mem, visited, estados_finais