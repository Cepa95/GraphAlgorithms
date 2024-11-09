def isEuler(graph):
    for vertex in graph:
        # print(graph[vertex])
        if len(graph[vertex]) % 2 != 0:
            return False
            '''ostatak'''
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
    
    print(isEuler(graph))

if __name__ == "__main__":
    main()
