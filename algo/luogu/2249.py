import sys
from bisect import bisect_left

def solve():
    input_data = (word for line in sys.stdin for word in line.split())
    n = int(next(input_data))
    m = int(next(input_data))
    nums = [int(next(input_data)) for _ in range(n)]
    results = []

    for _ in range(m):
        target = int(next(input_data))
        idx = bisect_left(nums, target)

        if idx < n and nums[idx] == target:
            results.append(str(idx + 1))
        else:
            results.append("-1")

    sys.stdout.write(' '.join(map(str, results)) + '\n')

if __name__ == "__main__":
    solve()
