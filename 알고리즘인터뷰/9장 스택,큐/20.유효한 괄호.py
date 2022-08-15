class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')':'(',   #닫히는 패턴일때
            '}':'{',
            ']':'['
        }
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False

        return len(stack) == 0