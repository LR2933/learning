import sys

def solve():
    s = list(map(int, sys.stdin.readline().split()))

    res = 0
    for i in range(4):
        tasks = list(map(int, sys.stdin.readline().split()))
        total_sum = sum(tasks)

        def dfs(idx, left):
            if left >= total_sum // 2 + 1:
                return left

            if idx == s[i]:
                return max(left, total_sum - left)
            else:
                return min(dfs(idx + 1, left + tasks[idx]), dfs(idx + 1, left))

        res += dfs(0, 0)

    print(res)

if __name__ == "__main__":
    solve()

