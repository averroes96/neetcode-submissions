"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        used_rooms = 0
        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])

        e_pointer = 0

        for start in starts:
            if start < ends[e_pointer]:
                used_rooms += 1
            else:
                e_pointer += 1

        return used_rooms
        