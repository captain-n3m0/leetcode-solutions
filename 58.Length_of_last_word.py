class Solution(object):
    def lengthOfLastWord(self, s):
        a=s.split()
        if len(a)==0:
            return 0
        else:
            return len(a[-1])

s="Hello World"
print(Solution().lengthOfLastWord(s))
