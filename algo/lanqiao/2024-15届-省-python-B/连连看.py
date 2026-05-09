import sys
from collections import defaultdict
def solve():
    input_data = sys.stdin.read().split()
    n, m = map(int, input_data[:2])

    matrx = []
    for i in range(n):
        start = i * m + 2
        matrx.append(input_data[start:start + m])

    main_digo = defaultdict(int)
    anti_digo = defaultdict(int)

    for i in range(n):
        for j in range(m):
            val = matrx[i][j]
            main_digo[(i + j, val)] += 1
            anti_digo[(i - j, val)] += 1

    ans = 0
    for i in main_digo.values():
        ans += i * (i - 1)
    for i in anti_digo.values():
        ans += i * (i - 1)

    print(ans)

if __name__ == "__main__":
    solve()

