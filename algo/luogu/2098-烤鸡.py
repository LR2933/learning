from itertools import product
def solve():
    n = int(input())

    if not (10 <= n <= 30):
        print(0)
        return

    possib = product([1, 2, 3], repeat= 10)

    ans = []
    for p in possib:
        if sum(p) == n:
            ans.append(p)

    print(len(ans))
    for i in ans:
        print(*i)


if __name__ == "__main__":
    solve()


