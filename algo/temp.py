import sys
from collections import deque

def solve():
    n, k = map(int, sys.stdin.readline().split())

    dist = [-1] * n
    queue = deque([0])
    dist[0] = 0

    while queue:
        curr = queue.popleft()

        next_nodes = [(curr + 1) % n, (curr + k) % n]

        for next_node in next_nodes:
            if dist[next_node] == -1:
                dist[next_node] = dist[curr] + 1
                queue.append(next_node)

    print(max(dist))

if __name__ == "__main__":
    solve()

