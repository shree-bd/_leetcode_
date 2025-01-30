class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Count character frequencies
        freq = Counter(s)
        max_heap = [(-cnt, char) for char, cnt in freq.items()]
        heapq.heapify(max_heap)  # Create max heap

        # Step 2: Check if reorganization is possible
        if any(-cnt > (len(s) + 1) // 2 for cnt, _ in max_heap):
            return ""

        res = []
        prev = None

        # Step 3: Construct the reorganized string
        while max_heap or prev:
            if prev and not max_heap:
                return ""  # If we can't place the previous character, return empty

            cnt, char = heapq.heappop(max_heap)
            res.append(char)
            cnt += 1  # Since stored as negative, adding 1 moves it towards zero

            if prev:
                heapq.heappush(max_heap, prev)  # Push back previous character
                prev = None

            if cnt != 0:
                prev = (cnt, char)  # Store current character for the next iteration

        return "".join(res)  # Convert list to string efficiently


# Time Complexity: O(n) (where n is the length of the input string)
# Space Complexity: O(n) (since the primary space is used by the result string)