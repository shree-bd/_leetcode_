class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_sum = (m+n)*mean
        curr_sum = sum(rolls)
        missing_sum = total_sum - curr_sum

        if missing_sum < n or missing_sum > 6* n:
            return []

        # Determine the average value for each missing roll
        base_value = missing_sum // n
        remainder = missing_sum % n
        
        # Create the list of missing rolls
        result = [base_value + 1] * remainder + [base_value] * (n - remainder)

        return result

        