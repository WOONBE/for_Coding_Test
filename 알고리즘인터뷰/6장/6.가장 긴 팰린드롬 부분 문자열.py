class Solution:
    def longestPalindrome(self, s: str) -> int:

        def expand(left: int, right: int) -> str:
            while left >=0 and right <len(s) and s[left] == s[right]:
                left -= 1
                right += 1    # 양쪽으로 한칸씩 확장해 나가면서 판단함
            return s[left + 1:right]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = '' #이부분 잘못 띄어쓰는 바람에 계산 오류가 났음

        for i in range(len(s) - 1):
            result = max(result,
                         expand(i,i+1),
                         expand(i,i+2),
                         key=len)

        return result