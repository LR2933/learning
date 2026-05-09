import sys
from itertools import combinations
def solve():
    n, r = map(int, sys.stdin.readline().split())
    
    comb = combinations(range(1, n + 1), r)

    for c in comb:
        for i in range(r):
            print(f"{c[i]:3}", end='')
        print()

if __name__ == "__main__":
    solve()

