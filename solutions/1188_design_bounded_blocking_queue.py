"""
1188. Design Bounded Blocking Queue
https://leetcode.com/problems/design-bounded-blocking-queue/
"""

from collections import deque
from threading import Semaphore, Lock


# METHOD 1: 2 semaphores
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


# METHOD 2: 2 semaphores, 1 lock
class BoundedBlockingQueue2(object):
    def __init__(self, capacity: int):
        self.queue = deque()
        self.push = Semaphore(capacity)
        self.pop = Semaphore(0)
        self.lock = Lock()

    def enqueue(self, element: int) -> None:
        self.push.acquire()
        self.lock.acquire()
        self.queue.append(element)
        self.lock.release()
        self.pop.release()

    def dequeue(self) -> int:
        self.pop.acquire()
        self.lock.acquire()
        element = self.queue.popleft()
        self.lock.release()
        self.push.release()
        return element

    def size(self) -> int:
        return len(self.queue)
