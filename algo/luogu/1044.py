import math
def solve():
    n = int(input().strip())
    print(math.comb(2 * n, n) // (n + 1))
if __name__ == '__main__':
    solve()
