class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # haystack=haystack.split()
        # for i in haystack:
        #     if 

        for i in range(0,len(haystack)-len(needle)+1):
            k=haystack[i:i+(len(needle))]
            if k==needle:
                return i
        else:
            return -1
            