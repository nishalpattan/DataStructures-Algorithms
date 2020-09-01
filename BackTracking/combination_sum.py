class Solution:
    def combinationSum(self, candidates, target):
        res = list()
        self.back_track(0, [], res, candidates, target)
        return res

    def back_track(self, idx, temp, res, candidates, target):
        if target == 0:
            res.append(temp[:])
        elif target > 0:
            for i in range(idx, len(candidates)):
                temp.append(candidates[i])
                self.back_track(i, temp, res, candidates, target - candidates[i])
                temp.pop()

if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([2,4,6,3],6))