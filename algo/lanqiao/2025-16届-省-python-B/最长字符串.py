import sys
from collections import defaultdict
def solve():
    input_data = sorted(list(set(sys.stdin.read().split())), key=len)
    result = defaultdict(list)
    beauties = defaultdict(set)

    for s in input_data:
        n = len(s)
        if n == 1:
            result[n].append(s)
            beauties[n].add(s)
        else:
            sorted_perfix = "".join(sorted(s[:-1]))
            if sorted_perfix in beauties[n - 1]:
                beauties[n].add("".join(sorted(s)))
                result[n].append(s)

    print("the ans is:")
    print(min((result[max(result)])))

if __name__ == "__main__":
    solve()
