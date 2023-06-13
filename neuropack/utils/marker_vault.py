from collections import defaultdict
from heapq import heappush, heappop, nsmallest
from typing import List, Tuple

class MarkerVault:
    def __init__(self) -> None:
        """A class to store markers and their timestamps. A marker can be any string.
        Allows to retrieve all timestamps for a given marker, and to retrieve all markers in chronological order.
        Optimized for fast retrieval of markers, at the cost of memory usage.
        """
        self._markers = defaultdict(list)
        self._sorted = defaultdict(lambda : False)
        self._timeline = list()
    
    def add_marker(self, marker: int, time: float):
        """Add a marker with a given timestamp. 
        The marker can be any string, the timestamp must be a number.
        The marker will be added to the timeline, and to the list of markers.

        :param marker: Marker to add, can be any positive number not zero
        :type marker: int
        :param time: Timestamp of the marker, must be a number
        :type time: float
        """
        assert marker > 0, "Marker must be a positive number"

        if time in self._markers[marker]:
            return
        self._markers[marker].append(time)
        self._sorted[marker] = False
        heappush(self._timeline, (time, marker))
    
    def get_marker(self, marker: int) -> List[float]:
        """Get all timestamps for a given marker.
        The timestamps will be sorted in ascending order.

        :param marker: Marker to retrieve
        :type marker: int
        :return: List of timestamps for the given marker in chronological order
        :rtype: List[float]
        """
        if not self._sorted[marker]:
            self._markers[marker].sort()
        self._sorted[marker] = True
        return self._markers[marker]

    def get_timeline(self) -> List[Tuple[float, int]]:
        """Get all markers in chronological order.
        The markers will be sorted in ascending order.

        :return: List of (timestamp, marker) tuples in chronological order
        :rtype: List[Tuple[float, int]]
        """
        return nsmallest(len(self._timeline), self._timeline)
    
    def __getitem__(self, marker: int):
        """Get all timestamps for a given marker.
        The timestamps will be sorted in ascending order.
        """
        return self.get_marker(marker)