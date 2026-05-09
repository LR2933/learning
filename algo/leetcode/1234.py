class Solution:
    def balancedString(self, s: str) -> int:
        min_length = len(s)
        left = 0
        count_letter = defaultdict(int)
        limit = len(s) // 4

        for i in s:
            count_letter[i] += 1
            
        if all(count_letter[x] == limit for x in 'QWER'):
            return 0

        for right, value_right in enumerate(s):
            count_letter[value_right] -= 1

            while left <= right and (count_letter['Q'] <= limit and count_letter['W'] <= limit and count_letter['E'] <= limit and count_letter['R'] <= limit):
                min_length = min(min_length, right - left + 1)
                
                count_letter[s[left]] += 1
                left += 1

        return min_length
