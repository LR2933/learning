from collections import defaultdict
import sys
def solve():
    input_data = sys.stdin.read().split()
    _, c = map(int, input_data[:2])
    count = defaultdict(int)
    nums = list(map(int, input_data[2:]))
    for i in nums:
        count[i] += 1

    ans = 0
    for i in count:
        target = c + i
        if target in count:
            ans += count[i] * count[target]

    print(ans)

if __name__ == "__main__":
    solve()

