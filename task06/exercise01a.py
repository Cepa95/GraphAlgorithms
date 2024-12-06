import networkx as nx
import time


def dijkstraAlgorithm(graph, source):
    if source not in graph:
        print(f"City {source} not found in the graph.")
        return
    startTime = time.time()
    lenghts, paths = nx.single_source_dijkstra(graph, source)

    print("Dijkstra Algorithm")
    resultTime = time.time() - startTime
    print(f"Time is: {resultTime}")

    return lenghts, paths


def bellmanFordAlgorithm(graph, source):
    if source not in graph:
        print(f"City {source} not found in the graph.")
        return
    startTime = time.time()
    lenghts, paths = nx.single_source_bellman_ford(graph, source)

    print("Bellman-Ford Algorithm")
    resultTime = time.time() - startTime
    print(f"Time is: {resultTime}")

    return lenghts, paths


def printLenghtsPaths(lenghts, paths):
    for target in paths:
        print(target)
        print(f"To {target}: Path: {paths[target]}, Distance: {lenghts[target]}")


def main():
    graph = nx.read_pajek("gradovi.net")
    # print(list(graph.nodes))
    # print(graph.edges)
    source = "LHR"
    lenghts, paths = dijkstraAlgorithm(graph, source)
    printLenghtsPaths(lenghts, paths)

    lenghts, paths = bellmanFordAlgorithm(graph, source)
    printLenghtsPaths(lenghts, paths)


if __name__ == "__main__":
    main()
