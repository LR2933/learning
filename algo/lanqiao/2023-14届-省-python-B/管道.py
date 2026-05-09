import sys
from collections import defaultdict
def solve():
    input_data = sys.stdin.read().split()
    n, length = map(int, input_data[:2])
    time_idx = defaultdict(list)
    for i in range(3, len(input_data), 2):
        time_idx[i].append(time_idx[i - 1])
    covered = set()
    for t in sorted(time_idx):



if __name__ == "__main__":
    solve()




