class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count


class Solution:
    """
    https://leetcode.com/problems/top-k-frequent-words/
    Efficient Approach
    TC : O(n * log k)
    SC : O(n)
    """

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hash_map = dict()
        heap = list()
        res = list()
        for word in words:
            hash_map[word] = hash_map.get(word, 0) + 1

        for word, freq in hash_map.items():
            heapq.heappush(heap, (Element(freq, word), word))
            if len(heap) > k:
                heapq.heappop(heap)
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res[::-1]

        """
        Heap Approach
        TC : O( n*logn + k*logn)
        SC : O(n)

        hash_map = dict()
        heap = list()
        res = list()
        for word in words:
            hash_map[word] = hash_map.get(word, 0) + 1

        # Building Max Heap --> O(n * logn), logn heappush operation on n words
        for word, freq in hash_map.items():
            heapq.heappush(heap, (-freq, word)) # performing heappush for n words

        # get k words from max heap --> O(k * logn) logn heappop operations k times
        for i in range(k):
            res.append(heapq.heappop(heap)[1]) 
        return res
      """