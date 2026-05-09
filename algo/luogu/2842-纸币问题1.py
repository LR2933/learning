import sys
def solve():
    input_data = sys.stdin.read().split()
    _, w = map(int, input_data[:2])
    coins = list(map(int, input_data[2:]))
    coins.sort()

    dp = [float('inf') for _ in range(w + 1)]
    dp[0] = 0

    for c in coins:
        for val in range(c, w + 1):
            if dp[val - c] != float('inf'):
                dp[val] = dp[val] if dp[val] < dp[val - c] + 1 else dp[val - c] + 1

    print(dp[-1])

if __name__ == "__main__":
    solve()
                
