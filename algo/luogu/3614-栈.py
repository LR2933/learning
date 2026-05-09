import sys
def solve():
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    result = []
    for _ in range(int(next(it))):
        stack = []
        for _ in range(int(next(it))):
            val = next(it)
            if val == 'push':
                stack.append(next(it))
            elif val == 'pop':
                if stack:
                    stack.pop()
                else:
                    result.append('Empty')
            elif val == 'query':
                if stack:
                    result.append(stack[-1])
                else:
                    result.append('Anguei!')
            elif val == 'size':
                result.append(str(len(stack)))

    sys.stdout.write('\n'.join(result))

if __name__ == "__main__":
    solve()

