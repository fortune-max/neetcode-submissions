class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for str in strs:
            ans += f"{chr(len(str))}{str}"
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        while s:
            str_lt = ord(s[0])
            ans.append(s[1:1+str_lt])
            s = s[1+str_lt:]
        return ans
