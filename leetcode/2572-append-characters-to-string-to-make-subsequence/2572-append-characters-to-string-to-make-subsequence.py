class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sample1 = list(s)
        sample2 = list(t)

        left1 = 0
        left2 = 0

        for _ in range(len(s)):
            if left2 < len(t) and sample1[left1] == sample2[left2]:
                left1 += 1
                left2 += 1
            else:
                left1 += 1

        return len(sample2) - left2