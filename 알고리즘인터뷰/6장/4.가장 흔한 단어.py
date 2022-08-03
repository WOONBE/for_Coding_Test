import collections
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]',' ', paragraph)
                 .lower().split()
                 if words not in banned] # data cleansing

        counts = collections.Counter(words)

        return counts.most_common(1)[0][0]