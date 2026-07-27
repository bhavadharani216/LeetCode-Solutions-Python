class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1 = sorted(s1)
        s2 = sorted(s2)

        canbreak1 = True
        canbreak2 = True

        for i in range(len(s1)):
            if(s1[i]< s2[i]):
                canbreak1 = False
            if s2[i] < s1[i]:
                canbreak2 = False

        return canbreak1 or canbreak2
