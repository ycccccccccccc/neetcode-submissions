class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = dict()
        sorted_strs = []

        n = 0
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in group_dict:
                group_dict[sorted_s] = n
                n += 1
            sorted_strs.append(sorted_s)

        output = [[] for i in range(len(group_dict))]
        for i, s in enumerate(sorted_strs):
            g = group_dict[s]
            output[g].append(strs[i])
        return output