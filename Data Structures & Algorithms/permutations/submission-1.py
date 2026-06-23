class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [["E"] * len(nums)]
        
        for num in nums:
            new = []
            for p in res:
                for i in range(len(nums)):
                    if p[i] == "E":
                        p[i] = num
                        new.append(p.copy())
                        p[i] = "E"
            res = new
        return res
