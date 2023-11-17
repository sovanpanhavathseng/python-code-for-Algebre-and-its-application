import threading

class Counter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.count += 1

    def decrement(self):
        with self.lock:
            self.count -= 1

    def get_count(self):
        return self.count

counter = Counter()

thread1 = threading.Thread(target=counter.increment)
thread2 = threading.Thread(target=counter.decrement)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(counter.get_count())  # Output: 0

import threading

def increment(count):
    # Use the `volatile` modifier to ensure that the write to count is visible to other threads
    count.value += 1

def decrement(count):
    # Use the `atomic` modifier to ensure that the write to count is visible to other threads
    count.value -= 1

def get_count(count):
    return count.value

count = threading.local()
count.value = 0

thread1 = threading.Thread(target=increment, args=(count,))
thread2 = threading.Thread(target=decrement, args=(count,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(get_count(count))  # Output: 0

import threading

class Counter:
    def __init__(self):
        self.count = 0
        self.replicas = []

    def increment(self):
        self.count += 1

        # Send the update to all replicas
        for replica in self.replicas:
            replica.increment()

    def decrement(self):
        self.count -= 1

        # Send the update to all replicas
        for replica in self.replicas:
            replica.decrement()

    def get_count(self):
        # Get the count from the local replica
        return self.count

counter = Counter()
replica1 = Counter()
replica2 = Counter()

counter.replicas.append(replica1)
counter.replicas.append(replica2)

thread1 = threading.Thread(target=counter.increment)
thread2 = threading.Thread(target=counter.decrement)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(replica1.get_count())  # Eventually outputs: 0
print(replica2.get_count())  # Eventually outputs: 0
