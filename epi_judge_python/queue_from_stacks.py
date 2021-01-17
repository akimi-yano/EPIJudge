from test_framework import generic_test
from test_framework.test_failure import TestFailure

# stack[0,1,3]
class Queue:
    def __init__(self):
        self.add_stack = []
        self.remove_stack = []
        
    def enqueue(self, x: int) -> None:
        self.add_stack.append(x)
    
    def dequeue(self) -> int:
        if not self.remove_stack:
            while self.add_stack:
                self.remove_stack.append(self.add_stack.pop())
        return self.remove_stack.pop()

def queue_tester(ops):
    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_from_stacks.py',
                                       'queue_from_stacks.tsv', queue_tester))
