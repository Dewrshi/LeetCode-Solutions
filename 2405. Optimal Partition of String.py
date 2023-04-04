class Solution:
    def partitionString(self, s: str) -> int:
        res = 0
        ss = ""
        for i in s:
            if i not in ss:
                ss += i
            else:
                res += 1
                ss = i
        return res + 1
      
#Solution 2:-------------------
class Solution:
    def partitionString(self, s: str) -> int:
        t=[*s]
        res=[]
        x=''
        for i in t:
            if i not in x:
                x+=i
            else:
                res.append(x)
                x=''.join(i)
        res.append(x)
        return len(res)
        
