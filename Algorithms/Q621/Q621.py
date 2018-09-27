class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dic = {}
        for task in tasks:
            dic[task] = dic.get(task, 0) + 1
        lst = list(dic.values())
        max_len = max(lst)
        max_len_count = lst.count(max_len)

        temp_res = (max_len - 1) * (n + 1) + max_len_count
        if temp_res >= len(tasks):
            return temp_res
        else:
            return len(tasks)
        



tasks = ["A","A","A","B","B","B"]
n = 0
print(Solution().leastInterval(tasks, n))