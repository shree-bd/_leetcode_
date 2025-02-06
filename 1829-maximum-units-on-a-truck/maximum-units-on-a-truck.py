class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x:x[1], reverse=True)
        max_units = 0

        for boxes, units in boxTypes:
            if truckSize == 0:
                break

            boxes_to_take = min(truckSize, boxes)
            max_units += boxes_to_take * units
            truckSize -= boxes_to_take
        return max_units
        