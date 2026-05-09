def solve():
    def to_b(x):
        return bin(x)[2:].count("1")

    def to_f(x):
        l = []
        while x != 0:
            l.append(x % 4)
            x //= 4

        return sum(l)

    count = 0
    for i in range(1, 2024 + 1):
        if to_b(i) == to_f(i):
            count += 1

    print(count)

if __name__ == "__main__":
    solve()
   
