class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_ct, s2_ct = len(s1), len(s2)
        if s1_ct > s2_ct:
            return False
        to_idx = lambda x: ord(x) - 97
        s1_arr = [0] * 26
        for c in s1:
            s1_arr[to_idx(c)] += 1
        s1_hsh = hash(tuple(s1_arr))

        s2_arr = [0] * 26
        for c in s2[:s1_ct]:
            s2_arr[to_idx(c)] += 1
        
        i = s1_ct - 1
        while i < s2_ct:
            if hash(tuple(s2_arr)) == s1_hsh:
                return True
            i += 1
            s2_arr[to_idx(s2[i-s1_ct])] -= 1
            if i < s2_ct:
                s2_arr[to_idx(s2[i])] += 1
        return False
