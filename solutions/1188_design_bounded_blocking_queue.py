"""
1188. Design Bounded Blocking Queue
https://leetcode.com/problems/design-bounded-blocking-queue/
"""

from collections import deque
from threading import Semaphore


class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.queue = deque()
        self.push = Semaphore(capacity)
        self.pop = Semaphore(0)

    def enqueue(self, element: int) -> None:
        self.push.acquire()
        self.queue.append(element)
        self.pop.release()

    def dequeue(self) -> int:
        self.pop.acquire()
        element = self.queue.popleft()
        self.push.release()
        return element

    def size(self) -> int:
        return len(self.queue)
