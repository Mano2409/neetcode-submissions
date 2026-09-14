class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        words.sort()

        for i in range(len(words)):
            sample = words[i]

            for j in range(len(words)):
                if i == j:
                    continue

                if sample in words[j]:
                    result.append(sample)
                    break

        return result