class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        # judge = []
        for x in strs:
            x = list(x)
            x_sorted = self.quicksort(x.copy())
            # x_sorted = sorted(x.copy())
            x = ''.join(x)
            x_sorted = ''.join(x_sorted)
            if x_sorted not in res:
                # judge.append(x_sorted)
                res[x_sorted] = []

            res[x_sorted].append(x)
        return list(res.values())

    def quicksort(self, lists):
        if len(lists) <= 1:
            return lists
        else:
            left = []
            right = []
            pivot = lists.pop()

            for x in lists:
                if x < pivot:
                    left.append(x)
                else:
                    right.append(x)
            return self.quicksort(left) + [pivot] + self.quicksort(right)


Input = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(Solution().groupAnagrams(Input))
