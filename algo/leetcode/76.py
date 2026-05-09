class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return t
        if len(s) < len(t):
            return ''

        count = Counter(t)
        target = len(count) 
        ans_left = -1
        ans_right = inf
        left = 0

        for right, value_right in enumerate(s):
            count[value_right] -= 1
            if count[value_right] == 0:
                target -= 1

            while target == 0:
                if right - left + 1 < ans_right - ans_left + 1:
                    ans_right = right
                    ans_left = left

                value_left = s[left]
                count[value_left] += 1
                if count[value_left] == 1:
                    target += 1 

                left += 1

        return '' if ans_left == -1 else s[ans_left:ans_right + 1]

