def solve():
    l, n, m = map(int, input().split())
    dis = [0]
    for _ in range(n):
        dis.append(int(input()))
    dis.append(l)
    shortest = 0
    longest = l
    result = float("inf")

    while shortest <= longest:
        mid = (shortest + longest) // 2
        count = 0
        last_stone = 0
        current_stone = 1

        while current_stone < n + 2:
            gap = dis[current_stone] - dis[last_stone]

            if gap < mid:
                count += 1 
                current_stone += 1
                if count > m:
                    longest = mid - 1
                    break
            else:
                last_stone = current_stone
                current_stone += 1

        if count <= m:
            result = mid
            shortest = mid + 1

    print(result)

if __name__ == "__main__":
    solve()

