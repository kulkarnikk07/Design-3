# Design-3

## Problem 1: Flatten Nested List Iterator (https://leetcode.com/problems/flatten-nested-list-iterator/)

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # A depth-first search function to flatten the nested list
        def flatten(nested_list):
            for element in nested_list:
                if element.isInteger():
                    # If the element is an integer, append it directly to flat_list
                    self.flat_list.append(element.getInteger())
                else:
                    # If the element is a list, recursively call flatten on it
                    flatten(element.getList())

        self.flat_list = []  # A list to store the flattened elements
        self.index = 0  # An index to track the current position in flat_list
        flatten(nestedList)  # Initialize by starting the flattening process
    
    def next(self) -> int:
        # Returns the next integer in the flat_list and increments the index
        value = self.flat_list[self.index]
        self.index += 1
        return value
    
    def hasNext(self) -> bool:
         # Check if there are more integers to iterate over
        return self.index < len(self.flat_list)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

## Problem 2: LRU Cache(https://leetcode.com/problems/lru-cache/)

class LRUCache:
    class Node:
        def __init__(self, key: int, value: int) -> None:
            self.key = key
            self.value = value
            self.next = None
            self.prev = None

    def addToHead(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node

    def removeNode(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashMap = dict()


    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1
        node = self.hashMap[key]
        self.removeNode(node)
        self.addToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            node = self.hashMap[key]
            self.removeNode(node)
            self.addToHead(node)
            node.value = value
            return
        if self.capacity == len(self.hashMap):
            tailPrev = self.tail.prev
            self.removeNode(tailPrev)
            del self.hashMap[tailPrev.key]
        node = self.Node(key, value)
        self.addToHead(node)
        self.hashMap[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)