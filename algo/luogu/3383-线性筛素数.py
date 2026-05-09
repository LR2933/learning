import sys

def sieve_of_eratosthenes(n):
    prime = bytearray([1]) * (n + 1)
    prime[0] = prime[1] = 0

    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            start = i * i
            num_elements = len(range(start, n + 1, i))
            prime[start:n + 1:i] = bytearray(num_elements)

    return [i for i, is_prime in enumerate(prime) if is_prime]

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    is_prime = sieve_of_eratosthenes(n)
    result = []
    for i in input_data[2:]:
        result.append(is_prime[int(i) - 1])
    sys.stdout.write('\n'.join(map(str, result)))

if __name__ == "__main__":
    solve()
