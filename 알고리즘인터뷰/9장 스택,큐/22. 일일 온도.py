class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T) #0으로 리스트 초기화
        stack = []

        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i) #높아질때까지 계속 스텍에 쌓다가 높아지는 값이 나오면 차이로 answer에 추가함


        return answer