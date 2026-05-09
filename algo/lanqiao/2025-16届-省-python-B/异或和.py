import sys

def solve():
    # 快速读入 (Fast I/O)
    input_data = sys.stdin.read().split()
    if not input_data: return
    n = int(input_data[0])
    a = list(map(int, input_data[1:]))

    total_ans = 0
    
    # 遍历二进制的每一位 (Iterate through each bit)
    for k in range(21): # 因为 a_i <= 2^20
        cnt0 = 0
        sum0 = 0
        cnt1 = 0
        sum1 = 0
        current_bit_contribution = 0
        
        for j in range(n):
            val = a[j]
            # 检查第 k 位是否为 1 (Check if the k-th bit is 1)
            if (val >> k) & 1:
                # 当前位是 1，找前面所有位是 0 的贡献
                # (j * count of 0s) - (sum of indices of 0s)
                # 注意：题目下标从 1 开始，所以这里用 j+1
                pos = j + 1
                current_bit_contribution += (pos * cnt0 - sum0)
                
                # 更新位为 1 的统计信息
                cnt1 += 1
                sum1 += pos
            else:
                # 当前位是 0，找前面所有位是 1 的贡献
                pos = j + 1
                current_bit_contribution += (pos * cnt1 - sum1)
                
                # 更新位为 0 的统计信息
                cnt0 += 1
                sum0 += pos
        
        # 将这一位的贡献累加到总答案中 (Add this bit's contribution to total)
        total_ans += current_bit_contribution * (1 << k)

    print(total_ans)

if __name__ == "__main__":
    solve()
