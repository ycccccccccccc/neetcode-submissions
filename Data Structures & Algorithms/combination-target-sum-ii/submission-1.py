class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        c = Counter(candidates)
        c_list = [[key, value] for key, value in c.items()]
        c_list.sort()

        subs = []
        def getSub(c_list: List[[int, int]], nums: List[int], index: int, target: int) -> None:
            nonlocal subs
            if target == 0:
                subs.append(nums)
                return
            
            if target < 0 or index >= len(c_list) or target < c_list[index][0]:
                return

            if c_list[index][1] > 0:
                c_list[index][1] -= 1
                getSub(c_list, nums + [c_list[index][0]], index, target-c_list[index][0])
                c_list[index][1] += 1

            getSub(c_list, nums, index+1, target)
        
        getSub(c_list, [], 0, target)
        return subs