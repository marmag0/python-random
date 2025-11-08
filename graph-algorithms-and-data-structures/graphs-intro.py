#!/usr/bin/env python3

#Class representation
class Node:
    def __init__(self, value, weigh=1, neighbors=None):
        self.val = value
        self.nb = neighbors if neighbors is not None else []
        self.weight = weigh

    def add_neighbor(self, node):
        self.nb.append((node))

def main():
    #Edge List representation (Lista Krawędzi) -> [F, T] (unidirectional) or [N1, N2] (bidirectional)
    #slow to iterate through
    graph1 = [
        [0, 1],
        [0, 2],
        [1, 2],
        [1, 3],
        [2, 3],
        [3, 4]
    ]

    #Adjacency Matrix representation (Macierz Sąsiedztwa)
    #consumes a lot of memory
    graph2 = [
        [0, 1, 1, 0, 0],  #node 0 connects to Node 1 and Node 2
        [0, 0, 1, 1, 0],  #node 1 connects to Node 2 and Node 3
        [0, 0, 0, 1, 0],  #node 2 connects to Node 3
        [0, 0, 0, 0, 1],  #node 3 connects to Node 4
        [0, 0, 0, 0, 0]   #node 4 has no outgoing edges
    ]

    #Adjacency List representation (Lista Sąsiedztwa)
    #hashmap
    graph3 = {
        0: [1, 2],  # node 0 connects to Node 1 and Node 2
        1: [2, 3],  # node 1 connects to Node 2 and Node 3
        2: [3],     # node 2 connects to Node 3
        3: [4],     # node 3 connects to Node 4
        4: []       # node 4 has no outgoing edges
    }

    return 0

if __name__ == "__main__":
    main()