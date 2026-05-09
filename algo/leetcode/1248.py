class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        ans = 0
        count = 0
        left = 0
       
        for right, right_value in enumerate(nums):
            if right_value % 2 != 0:
                count += 1
            
            remenber_left = left
            remenber_count = count

            while count >= k:
                if count == k:
                    ans += 1

                left_value = nums[left]

                if left_value % 2 != 0:
                    count -= 1

                left += 1

            left = remenber_left
            count = remenber_count
                
        return ans
