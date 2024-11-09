def countVerticles(graph):
    return len(graph)


def countEdges(graph):
    count = 0
    for verticle in graph:
        count += len(graph[verticle])
    return count // 2


def maxIncidentOfEdges(graph):
    maxBridges = 0
    maxVerticles = []

    for verticle in graph:
        bridge = len(graph[verticle])

        if bridge > maxBridges:
            maxBridges = bridge
            maxVerticles = [verticle]
        elif bridge == maxBridges:
            maxVerticles.append(verticle)
    return maxVerticles


def main():
    graph = {
        1: [2, 4, 5],
        2: [1, 3, 4, 5],
        3: [2, 4],
        4: [1, 2, 3, 5],
        5: [1, 2, 4]
    }

    print(countVerticles(graph))
    print(countEdges(graph))
    print(maxIncidentOfEdges(graph))


if __name__ == "__main__":
    main()
