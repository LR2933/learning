import sys
from collections import deque
def solve():
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    result = []
    de = deque()
    for _ in range(int(next(it))):
        val = next(it)
        if val == '1':
            de.append(next(it))
        elif val == '2':
            if de:
                de.popleft()
            else:
                result.append('ERR_CANNOT_POP')
        elif val == '3':
            if de:
                result.append(de[0])
            else:
                result.append('ERR_CANNOT_QUERY')
        elif val == '4':
            result.append(str(len(de)))

    sys.stdout.write('\n'.join(result))

if __name__ == "__main__":
    solve()


