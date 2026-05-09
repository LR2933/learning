def solve():
    n = int(input())

    a, b = 1, 2

    if n == 0:
        print(n)
        return
    elif n <= 2:
        print(n)
        return
    else:
        for _ in range(3, n + 1):
            a, b = b, a + b
        print(b)

if __name__ == "__main__":
    solve()
