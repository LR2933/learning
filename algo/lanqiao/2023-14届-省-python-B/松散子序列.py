import sys
def solve():
    s = sys.stdin.readline().strip()
    n = len(s)
    
    def get_value(c):
        return ord(c) - ord('a') + 1

    if len(s) == 1:
        print(get_value(s[0]))
        return

    dp = [0] * n
    dp[0] = get_value(s[0])
    dp[1] = get_value(s[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + get_value(s[i]))

    print(dp[-1])

if __name__ == "__main__":
    solve()
