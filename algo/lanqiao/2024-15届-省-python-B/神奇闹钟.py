import sys
from datetime import datetime, timedelta
def solve():
    input_data = sys.stdin.read().split()
    it_input = iter(input_data)
    fmt = '%Y-%m-%d %H:%M:%S'
    n = int(next(it_input))
    epoch = datetime(1970, 1, 1, 0, 0, 0)

    result = []
    for _ in range(n):
        time_str = next(it_input) + ' ' + next(it_input)
        time_obj = datetime.strptime(time_str, fmt).replace(second=0, microsecond=0)
        passed_time = time_obj - epoch
        passed_minute = int(passed_time.total_seconds()) // 60
        gap = int(next(it_input))
        offset = timedelta(minutes= passed_minute % gap)
        result.append(datetime.strftime(time_obj - offset, fmt))
    
    sys.stdout.write('\n'.join(result) + '\n')

if __name__ == "__main__":
    solve()
                           
