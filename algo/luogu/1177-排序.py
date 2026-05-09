import sys
input_data = sys.stdin.read().split()
n = input_data[0]
nums = list(map(int, input_data[1:]))
nums.sort()
print(*nums)
