class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        count1 = 0
        left = 0

        for right, value_right in enumerate(s):
            if value_right == "1":
                count1 += 1

            while count1 > k and right - left + 1 - count1 > k:
                if s[left] == '1':
                    count1 -= 1
                left += 1

            ans += right - left + 1

        return ans

