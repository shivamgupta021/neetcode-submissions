class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        checksum1 = [0] * 26
        checksum2 = [0] * 26

        for char in s1:
            checksum1[ord(char) - ord('a')] += 1

        for i in range(0, len(s1)):
            checksum2[ord(s2[i]) - ord('a')] += 1


        if checksum1 == checksum2:
            return True

        p1 = 0
        p2 = len(s1) - 1

        while p2 < len(s2):
            if checksum1 != checksum2:
                checksum2[ord(s2[p1]) - ord('a')] -= 1
                p1 += 1
                p2 += 1
                if p2 >= len(s2):
                    return False
                checksum2[ord(s2[p2]) - ord('a')] += 1
            else:
                return True

        return False