import sys
def next_permution(a):
    n = len(a)

    i = n - 2
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1

    if i == -1:
        return False

    j = n - 1
    while a[j] <= a[i]:
        j -= 1

    a[i], a[j] = a[j], a[i]
    a[i + 1:] = reversed(a[i + 1:])
    return True

def solve():
    input_data = sys.stdin.read().split()
    _, m = map(int, input_data[:2])
    a = list(map(int, input_data[2:]))
    for _ in range(m):
        next_permution(a)
    print(*a)


if __name__ == "__main__":
    solve()
