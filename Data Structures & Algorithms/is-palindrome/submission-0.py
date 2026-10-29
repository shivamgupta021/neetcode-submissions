class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue    
            c1 = s[start].lower()
            c2 = s[end].lower()
            if c1 != c2:
                print(c1, c2)
                return False
            start += 1
            end -= 1

        return True