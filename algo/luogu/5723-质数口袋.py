import sys
def solve():
    def is_prime(x):
        if 0 < x <= 2:
            return True
        elif x % 2 == 0:
            return False
        for i in range(3, int(x**0.5) + 1, 2):
            if x % i == 0:
                return False
        return True

    L = int(input().strip())
    count_sum = 0
    result = []
    for i in range(2, L + 1):
        if is_prime(i):
            count_sum += i
            if count_sum <= L:
                result.append(str(i))

    if result:
        sys.stdout.write('\n'.join(result) + '\n' + str(len(result)) + '\n')
    else:
        print(0)

if __name__ == "__main__":
    solve()

