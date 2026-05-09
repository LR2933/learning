def solve():
    l_limit = int(input())
    result = 0

    d = [0] * (l_limit + 1)
    for i in range(1, l_limit + 1):
        for j in range(i, l_limit + 1, i):
            d[j] += 1

    p = [0] * (l_limit + 1)
    for i in range(1, l_limit + 1):
        p[i] = d[i] + p[i - 1] 

    for i in range(1, l_limit):
        result += d[i] * p[l_limit - i]

    print(result)

if __name__ == "__main__":
    solve()
