class Solution:

    def encode(self, strs: List[str]) -> str:
        return "[" + ",".join(["'" + s + "'" for s in strs]) + "]"
    def decode(self, s: str) -> List[str]:
        if s == "[]": return []
        s = s.replace("['", "")
        s = s.replace("']", "")
        return s.split("','")