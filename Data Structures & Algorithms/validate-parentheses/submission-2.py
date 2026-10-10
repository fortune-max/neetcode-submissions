class Solution:
    def isValid(self, s: str) -> bool:
        opened, mapping = [None], { ')': '(', ']': '[', '}': '{' }

        for c in s:
            if c not in mapping:
                opened.append(c)
            else:
                if opened[-1] != mapping[c]:
                    return False
                opened.pop()
        return opened == [None]
