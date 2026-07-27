class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """

         

        def value(word):
            num = ""

            for ch in word:
                num += str(ord(ch) - ord('a'))

            return int(num)

        return value(firstWord) + value(secondWord) == value(targetWord)
        
