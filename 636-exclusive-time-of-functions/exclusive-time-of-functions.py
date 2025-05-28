class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n

        stack = []
        prev_start_time = 0

        for log in logs:
            func_id, call_type, timestamp = log.split(":")

            func_id = int(func_id)
            timestamp = int(timestamp)

            if call_type == "start":
                if stack:
                    result[stack[-1]] += timestamp -  prev_start_time

                stack.append(func_id)
                prev_start_time = timestamp

            else:
                result[stack.pop()] += timestamp - prev_start_time + 1
                prev_start_time = timestamp + 1

        return result

# T.C: O(N) | S.C : O(N)

        