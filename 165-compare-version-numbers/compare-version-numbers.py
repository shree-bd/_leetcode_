class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_parts = list(map(int, version1.split('.')))
        v2_parts = list(map(int, version2.split('.')))

        max_len = max(len(v1_parts), len(v2_parts))

        for i in range(max_len):
            num1 = v1_parts[i] if i < len(v1_parts) else 0
            num2 = v2_parts[i] if  i < len(v2_parts) else 0

            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        return 0
        