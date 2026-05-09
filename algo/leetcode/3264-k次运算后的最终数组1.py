class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = [(v, i) for i, v in enumerate(nums)]
        heapify(pq)

        for _ in range(k):
            val, i = heappop(pq)
            new_val = val * multiplier
            nums[i] = new_val
            heappush(pq, (new_val, i))

        return nums
