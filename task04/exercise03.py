def isEuler(graph):
    for vertex in graph:
        if len(graph[vertex]) % 2 != 0:
            return False
    visited = set()

    def dfs(v):
        visited.add(v)
        for neighbour in graph[v]:
            print("v", v)
            print(neighbour)
            print(graph[v])
            if neighbour not in visited:
                print("neighbour not visited", neighbour)
                dfs(neighbour)
    # pocetni vrh
    startVertex = list(graph.keys())[0]
    print("start", startVertex)
    dfs(startVertex)

    if len(visited) != len(graph):
        return False
    return True


def main():
    # graph = {
    #     1: [2, 4, 5],
    #     2: [1, 3, 4, 5],
    #     3: [2, 4],
    #     4: [1, 2, 3, 5],
    #     5: [1, 2, 4]
    # }

    graph = {
        1: [2, 5], 
        2: [1, 5], 
        3: [4, 5], 
        4: [3, 5], 
        5: [1, 2, 4, 3]
    }

    # graph = {
    #     1: [2, 5],
    #     2: [1, 5],
    #     3: [4, 5],
    #     4: [3, 5],
    #     5: [1, 2, 4, 3]
    # }

    print(isEuler(graph))


if __name__ == "__main__":
    main()
