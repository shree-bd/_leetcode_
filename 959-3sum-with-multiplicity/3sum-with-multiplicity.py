class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod = 10**9 + 7
        count = Counter(arr)
        result = 0
        
        # Sort the array to handle duplicates more easily
        unique_vals = sorted(count.keys())
        
        for i, num1 in enumerate(unique_vals):
            count_num1 = count[num1]
            for j in range(i, len(unique_vals)):
                num2 = unique_vals[j]
                num3 = target - num1 - num2
                
                if num3 < num2:
                    continue
                
                if num3 in count:
                    count_num2 = count[num2]
                    count_num3 = count[num3]
                    
                    if num1 == num2 == num3:
                        result += count_num1 * (count_num1 - 1) * (count_num1 - 2) // 6
                    elif num1 == num2 != num3:
                        result += count_num1 * (count_num1 - 1) // 2 * count_num3
                    elif num1 != num2 == num3:
                        result += count_num2 * (count_num2 - 1) // 2 * count_num1
                    elif num1 != num2 and num2 != num3:
                        result += count_num1 * count_num2 * count_num3
        
        return result % mod


