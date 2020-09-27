"""
Amazon Online Assessment Question
https://leetcode.com/discuss/interview-question/782606/
"""

import collections

def largest_item_association(item_association):
    hash_map = dict()
    group = list()

    for pair in item_association:
        if pair[0] in hash_map:
            hash_map[pair[0]].append(pair[1])
        else:
            hash_map[pair[0]] = [pair[1]]

        if pair[1] not in hash_map:
            hash_map[pair[1]] = []

    # BreadthFirstSearch
    for item in hash_map:
        q = collections.deque()
        q.append(item)
        curr_group = list()
        while q:
            curr_item = q.popleft()
            curr_group.append(curr_item)
            for next_item in hash_map[curr_item]:
                q.append(next_item)
        if len(group) < len(curr_group):
            group = curr_group
    group.sort()
    return group


if __name__ == "__main__":
    # example 1
    print(largest_item_association([
        ["item1","item2"],
        ["item3","item4"],
        ["item4","item5"]
    ]))
    print(largest_item_association([
        ['item1', 'item2'],
        ['item4', 'item5'],
        ['item3', 'item4'],
        ["item1", "item4"]]))

    print(largest_item_association(
        [
            ["item1", "item2"],
            ["item2", "item3"],
            ["item4", "item5"],
            ["item6", "item7"],
            ["item5", "item6"],
            ["item3", "item7"]
        ]
    ))
