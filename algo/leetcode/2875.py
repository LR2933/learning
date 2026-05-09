class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        sum_current = 0
        length_min = len(nums)
        left = 0
        is_found = False
        double_nums = nums * 2
        need_add = 0

        if sum(nums) < target:
            need_add = target // sum(nums) * n
            target = target % sum(nums)
        
        for right, value_right in enumerate(double_nums):
            sum_current += value_right

            while sum_current > target:
                sum_current -= double_nums[left]
                left += 1

            if sum_current == target:
                is_found = True
                length_min = min(length_min, right - left + 1)

        return length_min + need_add if is_found else -1
