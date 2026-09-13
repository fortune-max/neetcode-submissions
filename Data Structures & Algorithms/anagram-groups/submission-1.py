class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict as d
        dic = d(list)
        for idx, word in enumerate(strs, 0):
            rep = [0] * 26
            for char in word:
                rep[ord(char) - 97] += 1
            dic[str(rep)].append(idx)
        ans = []
        for key, idxes in dic.items():
            sub_arr = []
            for idx in idxes:
                sub_arr.append(strs[idx])
            ans.append(sub_arr)
        return ans
