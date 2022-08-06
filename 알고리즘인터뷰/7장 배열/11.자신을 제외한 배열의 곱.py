class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1

        for i in range(0, len(nums)): #왼쪽 값 곱하기
            out.append(p)
            p = p * nums[i]
        p = 1

        for i in range(len(nums) - 1, 0 -1, -1): #오른쪽 값 곱하기, 0-1해줘야 0자리까지 돌아준다
            out[i] = out[i] * p
            p = p * nums[i]

        return out