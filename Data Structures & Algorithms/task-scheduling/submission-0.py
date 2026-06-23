class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        note = [0] * 26
        for task in tasks:
            note[ord(task) - ord('A')] += 1

        max_f = max(note)
        
        n_max_f = note.count(max_f)
        
        ans = (max_f - 1) * (n + 1) + n_max_f
        return max(ans, len(tasks))

