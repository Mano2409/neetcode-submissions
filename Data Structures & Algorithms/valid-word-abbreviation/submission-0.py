class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if word == abbr:
            return True

        left1, left2 = 0, 0
        right = len(abbr)

        while left2 < right:

            if abbr[left2].isalpha():
                if left1 >= len(word):
                    return False

                if abbr[left2] == word[left1]:
                    left1 += 1
                    left2 += 1
                else:
                    return False

            else:
                if abbr[left2] == "0":
                    return False

                num = ""

                while left2 < right and abbr[left2].isdigit():
                    num += abbr[left2]
                    left2 += 1

                left1 += int(num)

        return left1 == len(word)