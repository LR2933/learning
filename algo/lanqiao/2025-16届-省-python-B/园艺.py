import sys
def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0]) 
    h = list(map(int, input_data[1:]))
    max_len = 0

    for step in range(1, n):
        for i in range(step, 2 * step):
            current_len = 1
            for j in range(i, n, step):
                if h[j] > h[j - step]:
                    current_len += 1
                    max_len = max(max_len, current_len)
                else:
                    current_len = 1

    print(max_len)

if __name__ == "__main__":
    solve()

