from test_framework import generic_test
from test_framework.test_failure import TestFailure

# n/s     
# [1, 2, 3]

# dequeue()
#  n     s
# [None, 2, 3]

# enqueue(4)
#    n/s
# [4, 2, 3]

# enqueue(5)
#
# [None, None, None, None, None, None]
#  s        n
# [2, 3, 4, None, None, None]
#  s           n
# [2, 3, 4, 5, None, None]

class Queue:
    def __init__(self, capacity: int) -> None:
        self.storage = [None] * max(capacity, 1)
        self.count = 0
        self.start = 0
        self.next = 0

    def enqueue(self, x: int) -> None:
        if self.count >= len(self.storage):
            self.resize()
        self.storage[self.next] = x
        self.next = (self.next + 1) % len(self.storage)
        self.count += 1

    def dequeue(self) -> int:
        val = self.storage[self.start]
        self.storage[self.start] = None
        self.start = (self.start + 1) % len(self.storage)
        self.count -= 1
        return val

    def size(self) -> int:
        return self.count
    
    def resize(self):
        new_storage = [None] * len(self.storage) * 2
        for i in range(self.count):
            new_storage[i] = self.storage[(self.start+i) % len(self.storage)]
        self.storage = new_storage
        self.start, self.next = 0, self.count

def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
