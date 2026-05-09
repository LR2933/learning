import sys
def solve():
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    t = int(next(it))
    result = []

    for _ in range(t):
        n = int(next(it))

        ans = 0
        if n % 3 == 0:
            ans += 2 * n
        else:
            ans += n

        result.append(str(ans))

    sys.stdout.write('\n'.join(result) + '\n')

if __name__ == "__main__":
    solve()

