from linkedlist import *

class Node:
    
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
        
class PriorityQueue:

    def __init__(self):
        self.items = LinkedList()
        self.length = 0
        self.frontIdx = 0

    def isEmpty(self):
        return (self.length == 0)

    def __len__(self):
        return len(self.items)

    def enqueue(self, thing, p):
        noodle = Node(thing, p)
        if self.length == 0:
            self.items.append(noodle)
            self.length += 1
            return
        
        for i in range(self.frontIdx, self.length+self.frontIdx):
            if noodle.priority >= self.items[i].priority:
                self.items.insert(i, noodle)
                self.length += 1
                return

        self.items.append(noodle)
        self.length += 1
        return        
    
    def dequeue(self):
        item = self.items[self.frontIdx].item
        self.frontIdx += 1
        self.length -= 1
        return item
    
    def front(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to access front of empty queue")
        
        return self.items[self.frontIdx].item
    
    def front_priority(self):
        return self.items[self.frontIdx].priority
    
def main():
    pq = PriorityQueue()
    pq.enqueue('a', 0.25)
    pq.enqueue('b', 0.25)
    print(pq.dequeue())


if __name__ == "__main__":
    main()