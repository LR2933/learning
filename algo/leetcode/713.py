class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0 or k == 1:
            return 0

        count = 0
        left = 0
        product = 1

        for right, value_right in enumerate(nums):
            product *= value_right

            while product >= k:
                product //= nums[left]
                left += 1

            if product < k:
                count += right - left + 1

        return count

