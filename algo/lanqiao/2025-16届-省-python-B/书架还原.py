import sys
def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    nums = list(map(int, input_data[1:]))
    count = 0

    pos = {value:idx for idx, value in enumerate(nums)}

    for current_pos in range(n):
        target_val = current_pos + 1
        target_val_pos = pos[target_val]
        if nums[current_pos] != target_val:
            nums[current_pos], nums[target_val_pos] = nums[target_val_pos], nums[current_pos]
            pos[nums[target_val_pos]] = target_val_pos
            count += 1

    print(count)

if __name__ == "__main__":
    solve()

