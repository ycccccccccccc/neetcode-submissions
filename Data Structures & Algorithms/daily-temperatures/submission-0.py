class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t_map = [temperatures[0]]
        d_map = [0]
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if t > t_map[-1]:
                while t_map and t > t_map[-1]:
                    t_map.pop()
                    d = d_map[-1]
                    result[d] = i - d
                    d_map.pop()
            t_map.append(t)
            d_map.append(i)
                
        return result