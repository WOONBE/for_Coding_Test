import collections

class Solution:

    def isPalindrome(self, s: str) -> bool:

        strs : Deque = collections.deque() #시간 절약용

        for char in s:
            if char.isalnum(): #문자형식만 추가
                strs.append(char.lower()) #소문자로 추가


        while len(strs)>1:
            if strs.popleft() != strs.pop():
                return False

        return True



