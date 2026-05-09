class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapify_max(gifts)
        while k > 0 and gifts[0] != 1:
            heapreplace_max(gifts, isqrt(gifts[0]))
            k -= 1
        return sum(gifts)
