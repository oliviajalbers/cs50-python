class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("capacity must be a non negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if (n + self.size) > self.capacity:
            raise ValueError("Exceeds capacity")
        self._size = self.size + n


    def withdraw(self, n):
        if (self.size-n) < 0:
            raise ValueError("Not enough cookies")
        self._size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
"""
jar = Jar(30)
jar.deposit(3)
jar.withdraw(10)
print(jar)
"""
