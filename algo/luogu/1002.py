def solve():
    b_x, b_y, h_x, h_y = map(int, input().split())

    forbidden = set()
    forbidden.add((h_x, h_y))
    offsets = [
        (1, 2), (1, -2), (-1, 2), (-1, -2), 
        (2, 1), (2, -1), (-2, 1), (-2, -1)
               ]
    for x, y in offsets:
        n_x, n_y = h_x + x, h_y + y
        if n_x >= 0 and n_y >= 0:
            forbidden.add((n_x, n_y))

    dp = [[0] * (b_y + 1) for _ in range(b_x + 1)]

    if (0, 0) not in forbidden:
        dp[0][0] = 1

    for i in range(b_x + 1):
        for j in range(b_y + 1):
            if i == 0 and j == 0 or (i, j) in forbidden:
                continue

            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
            

    print(dp[b_x][b_y])

if __name__ == "__main__":
    solve()
