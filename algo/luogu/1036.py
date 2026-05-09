import sys
import itertools
def solve():
    input_data = sys.stdin.read().split()
    k = int(input_data[1])
    nums = [int(x) for x in input_data[2:]]
    ans = 0
    memo_prime = set()
    memo_not_prime = set()

    def is_prime(x):
        if x in memo_prime:return True
        elif x in memo_not_prime:return False

        if x < 2:return False
        if x == 2:return True
        if x % 2 == 0:return False
        limit = int(x ** 0.5) + 1
        for i in range(3, limit, 2):
            if x % i == 0:
                memo_not_prime.add(x)
                return False
        memo_prime.add(x)
        return True

    for combo in itertools.combinations(nums, k):
        if is_prime(sum(combo)):
            ans += 1

    print(ans)

if __name__ == "__main__":
    solve()
