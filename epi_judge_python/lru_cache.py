from test_framework import generic_test
from test_framework.test_failure import TestFailure

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
class LruCache:
    def __init__(self, capacity: int) -> None:
        self.cache = {}
        self.capacity = capacity
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def lookup(self, isbn: int) -> int:
        # if we have it , return the price & update the node (remove from whereever it is and add to from)
        if isbn in self.cache:
            node = self.cache[isbn]
            self.remove_node(node)
            self.add_to_head(node)
            return node.value
        # if not return -1
        else:
            return -1

    def insert(self, isbn: int, price: int) -> None:
        # if isbn already present, it should not update the price but make it th most recently used entry (by calling self.lookup)
        # if not add (to the front) 
        if self.lookup(isbn) == -1:
            new_node = Node(isbn, price)
            self.cache[isbn] = new_node
            self.add_to_head(new_node)
            if len(self.cache) > self.capacity:
                node_to_remove = self.tail.prev
                dict_key = self.tail.prev.key 
                self.remove_node(node_to_remove)
                del self.cache[dict_key]

    def erase(self, isbn: int) -> bool:
        # remove the isbn and the price and return True if exists
        if isbn in self.cache:
            node_to_erase = self.cache[isbn]
            key_to_erase = node_to_erase.key
            self.remove_node(node_to_erase)
            del self.cache[key_to_erase]
            return True
        # else return False 
        else:
            return False

    def remove_node(self, node):
        # prevnode node nextnode
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = None
        node.next = None        

    def add_to_head(self, node):
        # head node next_node 
        next_node = self.head.next
        next_node.prev = node 
        self.head.next = node 
        node.prev = self.head 
        node.next = next_node        


def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure('Lookup: expected ' + str(cmd[2]) +
                                  ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure('Erase: expected ' + str(cmd[2]) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lru_cache.py', 'lru_cache.tsv',
                                       lru_cache_tester))
