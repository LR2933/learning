import sys

read = True
comp_info = []

while read:
    s = sys.stdin.readline().strip().split()

    if 'E' in s:
        index = s.index('E')
        comp_info.append(s[0:index])
        read = False
    else:
        comp_info.append(s)


scores11 = [0,0]
scores21 = [0,0]
n = len(comp_info)
for _ in range(n):


