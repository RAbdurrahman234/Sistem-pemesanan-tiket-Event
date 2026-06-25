# LINKEDLIST -------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
        self.tail = node
        if not self.head:
            self.head = node
        self.size += 1

    def dequeue(self):
        if not self.head:
            return None
        data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.size -= 1
        return data

    def is_empty(self):
        return self.size == 0

# HASHMAP --------------------------------------

class HashMap:
    def __init__(self, kapasitas=64):
        self.kapasitas = kapasitas
        self.bucket = [[] for _ in range(kapasitas)]

    def _hash(self, key):
        total = 0
        for ch in str(key):
            total = (total * 31 + ord(ch)) % self.kapasitas
        return total

    def set(self, key, value):
        i = self._hash(key)
        for j, (k, _) in enumerate(self.bucket[i]):
            if k == key:
                self.bucket[i][j] = (key, value)
                return
        self.bucket[i].append((key, value))

    def get(self, key):
        for k, v in self.bucket[self._hash(key)]:
            if k == key:
                return v
        return None
