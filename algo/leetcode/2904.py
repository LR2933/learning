class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count('1') < k:
            return ''

        shortest_substring = s
        left = 0
        count_one = 0


        for right, value_right  in enumerate(s):
            count_one += int(value_right)

            while count_one == k:
                temp_substring = s[left:right + 1]

                if len(temp_substring) < len(shortest_substring) or (len(temp_substring) == len(shortest_substring) and temp_substring < shortest_substring):
                    shortest_substring = temp_substring 

                if s[left] == '1':
                    count_one -= 1

                left += 1

        return shortest_substring


