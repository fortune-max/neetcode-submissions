class Solution:
    def isValid(self, s: str) -> bool:
        open_chars, close_chars = "([{", ")]}"
        opened = []

        for c in s:
            if c in open_chars:
                opened.append(c)
            else:
                mirror = open_chars[close_chars.index(c)]
                if opened and opened[-1] == mirror:
                    opened.pop()
                else:
                    return False
        return not bool(opened)
