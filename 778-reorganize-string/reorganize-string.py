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


# Other good solution
class Solution:
    def reorganizeString(self, s: str) -> str:
        #we want to pair the ones with the highest frequency first
        #each time we will pop the first two items from the heap
        #we only add it back to the heap if freq + 1 is > 0, meaning we still have letters to pair
        #our heap will be while len(heap) > 1, while our heap has more than one letter
        #now that our heap has only one letter left, there must be one count of that letter, if there is 
        #more than one, we cannot place it side by side
        counts = Counter(s)
        maxHeap = [(-freq, letter) for letter, freq in counts.items()]
        heapify(maxHeap)

        res = []
        while len(maxHeap) > 1:
            freq1, char1 = heappop(maxHeap)
            freq2, char2 = heappop(maxHeap)
            
            res.extend([char1, char2])

            if freq1 + 1 < 0:
                heappush(maxHeap, (freq1 + 1, char1))
            if freq2 + 1 < 0:
                heappush(maxHeap, (freq2 + 1, char2))
        
        if maxHeap:
            freq, char = heappop(maxHeap)
            if freq + 1 < 0:
                return ""
            res.append(char)
        
        return "".join(res)
            
            