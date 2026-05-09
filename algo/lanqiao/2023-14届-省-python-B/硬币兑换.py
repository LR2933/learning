def solve():
    n = 2022
    count = [0 for _ in range(n * 2 + 1)]

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if i == j:
                count[i + j] += i // 2
            else:
                count[i + j] += i

    print(f"count:{max(count)}")
    print(f"value:{count.index(max(count))}")


if __name__ == "__main__":
    solve()

