import sys
from itertools import permutations
def solve():
    input_data = sys.stdin.read().split()[0]
    words = set()
    count = 0
    perms = permutations(['l', 'q', 'b'])

    for p in perms:
        words.add(''.join(p))

    i = 3
    while i <= len(input_data):
        if input_data[i - 3: i] in words:
            count += 1
            i += 3
        else:
            i += 1

    print(count)

if __name__ == "__main__":
    solve()

