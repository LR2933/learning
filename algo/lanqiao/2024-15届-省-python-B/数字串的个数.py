def solve():
    n = 10000
    m = 10 ** 9 + 7
    total = pow(9, n, m)
    no_3 = pow(8, n, m)
    no_7 = pow(8, n, m)
    no_both = pow(7, n, m)
    ans = (total - no_3 - no_7 + no_both) % m
    print(ans)

if __name__ == "__main__":
    solve()
    

