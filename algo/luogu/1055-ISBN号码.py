import sys
def solve():
    ss = sys.stdin.readline().strip()
    num_sum = 0
    idx = 1
    for i in range(len(ss) - 1):
        if '0' <= ss[i] <= '9':
            num_sum += int(ss[i]) * idx
            idx += 1
    c = num_sum % 11
    if c == 10:
        c = 'X'
    else:
        c = str(c)

    if ss[-1] == c:
        print("Right")
    else:
        print(ss[:-1] + c)

if __name__ == "__main__":
    solve()

