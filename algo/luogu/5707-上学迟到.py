import sys
from datetime import datetime, timedelta
def solve():
    input_data = sys.stdin.read().split()
    s, v = map(int, input_data[:2])
    time_need = (s + v - 1) // v + 10
    offset = timedelta(minutes=time_need)
    target_time = datetime(1970, 1, 2, 8, 0, 0)
    ans = target_time - offset
    fmt = '%H:%M'
    print(ans.strftime(fmt))

if __name__ == "__main__":
    solve()

