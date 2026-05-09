import sys
from collections import deque
def solve():
    n = int(sys.stdin.readline().strip())
    grid = [list(sys.stdin.readline().strip()) for _ in range(n)]
    is_visited = [[False] * n for _ in range(n)]

    total_island = 0
    survived_island = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(n):
        for j in range(n):
            if grid[i][j] == '#' and not is_visited[i][j]:
                is_visited[i][j] = True
                total_island += 1
                is_survived = False


                queue = deque([(i, j)])


                while queue:
                    cx, cy = queue.popleft()

                    is_safe = True
                    for k in range(4):
                        nx, ny = cx + dx[k], cy + dy[k]
                        if grid[nx][ny] == '.':
                            is_safe = False
                            break

                    if is_safe:
                        is_survived = True

                    for k in range(4):
                        nx, ny = cx + dx[k], cy + dy[k]
                        if n > nx > 0 and n > ny > 0 and grid[nx][ny] == '#' and not is_visited[nx][ny]:
                            is_visited[nx][ny] = True
                            queue.append((nx, ny))

                if is_survived:
                    survived_island += 1

    print(total_island - survived_island)

if __name__ == "__main__":
    solve()

