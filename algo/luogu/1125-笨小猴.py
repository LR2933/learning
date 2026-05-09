from collections import defaultdict
s = input().strip()
count = defaultdict(int)

for i in s:
    count[i] += 1

def is_prime(x):
    if x == 2:
        return True
    elif x < 2 or x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5), 2):
        if x % i == 0:
            return False
    return True
    
check = max(count.values()) - min(count.values())
if is_prime(check):
    print('Lucky Word')
    print(check)
else:
    print('No Answer')
    print(0)

