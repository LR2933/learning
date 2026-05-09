import sys

def next_permutation(a):
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
    a[i + 1:] = a[i + 1:][::-1]
    return True

def solve():
    n = int(sys.stdin.readline().strip())
    ll = list(range(1, n + 1))
    print(''.join([f'{i:5}'for i in ll]))
    while next_permutation(ll):
        print(''.join([f'{i:5}'for i in ll]))

if __name__ == "__main__":
    solve()
