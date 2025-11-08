#! /usr/bin/env python3

#PiAA egzam 2024/2025 - I

from collections import deque

def odd_path(G, A, B):
    n = len(G)
    visited = [[False, False] for _ in range(n + 1)]
    queue = deque()
    
    queue.append((A, 0, [A]))
    visited[A][0] = True

    while queue:
        current, parity, path = queue.popleft()
        
        for neighbor in G[current - 1]:
            next_parity = 1 - parity
            if not visited[neighbor][next_parity]:
                visited[neighbor][next_parity] = True
                new_path = path + [neighbor]
                if neighbor == B and next_parity == 1:
                    return new_path
                queue.append((neighbor, next_parity, new_path))
    
    return -1

def main():
    G1 = [[2,3,7],[1,4,8],[1,4,5],[2,3,6],[3,6,7],[4,5,8],[1,5,8],[2,6,7]]
    print(odd_path(G1, 7, 2))

    G2 = [[2,3,4,5],[1,4],[1,5],[2,1,5],[1,3,4]]
    print(odd_path(G2, 2, 3))

    G3 = [[4],[3,4],[2,4],[1,2,3,5],[4]]
    print(odd_path(G3, 1, 5))
    return 0

if __name__ == "__main__":
    main()

    