class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = [0] * 26
        y = [0] * 26
        for word in s:
            x[ord(word) - ord('a')] += 1
        for word in t:
            y[ord(word) - ord('a')] += 1
        
        return x == y