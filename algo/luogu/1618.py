a, b, c = map(int, input().strip().split())
is_found = False

if a != 0 and b != 0 and c != 0:
    for i in range(123, 999):
        if i * b % a == 0 and i * c % a == 0:
            j = i * b // a
            k = i * c // a

            if j <= 999 and k <= 999:
                combined = str(i) + str(j) + str(k)
                if len(combined) == 9 and '0' not in combined and len(set(combined)) == 9:
                    print(i, j, k)
                    is_found = True

if not is_found:
    print("No!!!")
    
