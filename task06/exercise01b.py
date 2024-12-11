import networkx as nx
import time


"""Napisati program koji traži najkraći put između dva grada koristeći:
(a) Greedy BFS
(b) A* algoritam
"""


def heuristic(graph, node, neighbor):
    weight = list(graph[node][neighbor].values())[0].get("weight")
    return weight


def greedyBFSAlgorithm(graph, source, target):
    if source not in graph:
        print(f"City {source} not found in the graph.")
        return None
    if target not in graph:
        print(f"City {target} not found in the graph.")
        return None

    startTime = time.time()

    visited = set()
    priorityQueue = [(0, source, [source])]

    while priorityQueue:
        priorityQueue.sort(key=lambda x: x[0])
        _, node, path = priorityQueue.pop(0)

        if node == target:
            resultTime = time.time() - startTime
            print("Greedy BFS Algorithm")
            print(f"Time is: {resultTime}")
            return path

        if node not in visited:
            visited.add(node)
            neighbors = list(graph.neighbors(node))

            neighbors.sort(key=lambda neighbor: heuristic(graph, node, neighbor))

            for neighbor in neighbors:
                if neighbor not in visited:
                    newPath = path + [neighbor]
                    priority = heuristic(graph, node, neighbor)
                    priorityQueue.append((priority, neighbor, newPath))

    return None


def aStarAlgorithm(graph, source, target):
    if source not in graph:
        print(f"City {source} not found in the graph.")
        return
    if target not in graph:
        print(f"City {target} not found in the graph.")
        return
    startTime = time.time()
    path = nx.astar_path(graph, source, target)

    print("A* Algorithm")
    resultTime = time.time() - startTime
    print(f"Time is: {resultTime}")

    return path


def printPath(path, target, source):
    if path:
        print(f"To {target}: from: {source}, shorthest path: {path}")
    else:
        print(f"No path found between {source} and {target}.")


def main():
    graph = nx.read_pajek("gradovi.net")
    # print(list(graph.nodes))
    # print(graph.edges)
    source = "LHR"
    target = "BER"
    path = greedyBFSAlgorithm(graph, source, target)
    printPath(path, target, source)

    path = aStarAlgorithm(graph, source, target)
    printPath(path, target, source)


if __name__ == "__main__":
    main()
