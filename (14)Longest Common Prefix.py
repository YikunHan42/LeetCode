class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        for i in range(1, len(strs), 1):
            ls = []
            if(len(strs[i]) == 0):
                pre = ""
                return pre
            num = min(len(pre), (len(strs[i])))
            for j in range(num):
                if(pre[j] == strs[i][j]):
                    ls.append(strs[i][j])
                else:
                    pre = "".join(ls)
                    break
                if(j == num - 1): pre = "".join(ls)
        return pre