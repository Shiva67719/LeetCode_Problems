class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        if target>=letters[-1] or target<letters[0]:
            return letters[0]
        s=0
        e=len(letters)-1
        while s<=e:
            mid=(s+e)//2
            if target>=letters[mid]:
                s=mid+1
            else:
                e=mid-1
        return letters[s]