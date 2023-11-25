class Solution:
    def defangIPaddr(self, address: str) -> str:
        a = address.split(".")
        return "[.]".join(a)
