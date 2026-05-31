from collections import deque

class LeakyBucket:
    def __init__(self, capacity, leak_rate):
        self.capacity = capacity      # max packets in bucket
        self.leak_rate = leak_rate    # packets processed per leak()
        self.bucket = deque()

    def add_packet(self, packet):
        if len(self.bucket) < self.capacity:
            self.bucket.append(packet)
            print(f"Packet {packet} added")
        else:
            print(f"Packet {packet} dropped (bucket full)")

    def leak(self):
        for _ in range(min(self.leak_rate, len(self.bucket))):
            packet = self.bucket.popleft()
            print(f"Processed packet {packet}")