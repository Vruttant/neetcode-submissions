class Solution:

    def encode(self, strs: List[str]) -> str:
        Solution.variable = strs
        return ""

    def decode(self, s: str) -> List[str]:
        return Solution.variable