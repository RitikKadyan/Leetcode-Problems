class Solution(object):
    def lengthOfLastWord(self, s):
        if s.isspace():
            return 0
        else:
            words = s.split()
            return len(words[-1])
