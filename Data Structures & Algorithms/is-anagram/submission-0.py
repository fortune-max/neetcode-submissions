class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, s2 = [0] * 26, [0] * 26
        for c in s:
            s1[ord(c) - 97] += 1
        for c in t:
            s2[ord(c) - 97] += 1
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                return False
        return True