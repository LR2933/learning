hp = 2025
count = 0
while hp > 0:
    count += 1
    hp -= 5
    if count % 2 == 1:
        hp -= 15
    else:
        hp -= 2
    if count % 3 == 1:
        hp -= 2
    elif count % 3 == 2:
        hp -= 10
    else:
        hp -= 7

print(count)


