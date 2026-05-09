import sys
def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    s = input_data[1: n + 1]
    t = input_data[n + 1: 2 * n + 1]

    maping = {'0':0, '2':1, '4':2}
    dp_s = [-float('inf')] * 3
    dp_t = [-float('inf')] * 3
    res_val = 0

    for i in range(n):
        current_max_s = -float('inf')
        current_max_t = -float('inf')

        digit_s = {maping[d] for d in s[i] if d in maping}
        digit_t = {maping[d] for d in t[i] if d in maping} 

        if digit_s:
            current_max_s = 1
            for d in digit_s:
                current_max_s = max(current_max_s, dp_t[d] + 1)


        if digit_t:
            for d in digit_t:
                current_max_t = max(current_max_t, dp_s[d] + 1)

        for d in digit_s:
            dp_s[d] = max(current_max_s, dp_s[d])

        for d in digit_t:
            dp_t[d] = max(current_max_t, dp_t[d])

        res_val = max(res_val, current_max_s, current_max_t)

    print(res_val)

if __name__ == "__main__":
    solve()

