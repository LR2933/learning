def solve():
    _, m = map(int, input().strip().split())
    tree_tall = list(map(int, input().split()))
    tallest = max(tree_tall)
    lowest = 0
    result = -1

    while lowest <= tallest:
        mid = (tallest + lowest) // 2
        mood = sum(max(0, x - mid) for x in tree_tall)
        if mood >= m:
            lowest = mid + 1
            result = mid
        else:
            tallest = mid - 1

    print(result)

if __name__ == "__main__":
    solve()

