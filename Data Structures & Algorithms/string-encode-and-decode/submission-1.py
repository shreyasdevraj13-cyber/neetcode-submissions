class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            s = ""

        s = ""
        for word in strs:
            s += "5#"
            s += word
        return s

    def decode(self, s: str) -> List[str]:
        if s == "":
            t = []
            return t
        t = s[2:]
        res = t.split("5#") 
        return res
