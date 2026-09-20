class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [x for x in s.lower() if 96 < ord(x) < 123 or 47 < ord(x) < 58]
        if not len(s):
            return True
        for i in range(len(s)//2 + 1):
            lhs, rhs = i, -i-1
            if s[lhs] != s[rhs]:
                ans = False
                break
        else:
            ans = True
        return ans
