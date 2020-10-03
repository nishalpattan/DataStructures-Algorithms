class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        """
        https://leetcode.com/problems/kill-process/
        TC : O(n)
        SC : O(n)
        """
        hash_map = dict()
        res = list()
        for idx, process_id in enumerate(ppid):
            if process_id in hash_map:
                hash_map[process_id].append(pid[idx])
            else:
                hash_map[process_id] = [pid[idx]]

        to_kill = [kill]
        while to_kill:
            kill_id = to_kill.pop()
            res.append(kill_id)
            if kill_id in hash_map:
                to_kill += hash_map[kill_id]
        return res