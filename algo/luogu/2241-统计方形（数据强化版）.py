import sys
def solve():
    n, m = map(int, sys.stdin.readline().split())

    count_rect = sum(range(1, n + 1)) *sum(range(1, m + 1))

    count_squre = 0
    for i in range(1, min(n, m) + 1):
        count_squre += (n - i + 1) * (m - i + 1)

    
    print(count_squre, count_rect - count_squre)

if __name__ == "__main__":
    solve()


