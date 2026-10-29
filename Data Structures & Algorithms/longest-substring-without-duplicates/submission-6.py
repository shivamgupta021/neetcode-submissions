class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        ans = 1
        unique = set()
        ptr1 = 0
        unique.add(s[ptr1])
        ptr2 = 1

        while ptr2 < n:
            if s[ptr2] in unique:
                ans = max(ans, ptr2 - ptr1)
                unique.remove(s[ptr1])
                ptr1 += 1
            else:
                unique.add(s[ptr2])
                ptr2 += 1

        return max(ans, ptr2 - ptr1)