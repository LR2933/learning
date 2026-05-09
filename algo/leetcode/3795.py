class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        min_length = len(nums)
        sum_nums = 0
        left = 0
        count_nums = [0] * (max(nums) + 1)
        flag = False

        for right, value_right in enumerate(nums):
            count_nums[value_right] += 1
            if count_nums[value_right] == 1:
                sum_nums += value_right

            while sum_nums >= k and left <= right:
                flag = True
                min_length = min(min_length, right - left + 1)
                value_left = nums[left]
                count_nums[value_left] -= 1
                if count_nums[value_left] == 0:
                    sum_nums -= value_left
                left += 1

        return min_length if flag else -1
