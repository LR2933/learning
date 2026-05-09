import sys
def solve():
    a, b, p = map(int, sys.stdin.read().split())
    ans = pow(a, b, p)
    sys.stdout.write(f'{a}^{b} mod {p}={ans}')

if __name__ == "__main__":
    solve()

