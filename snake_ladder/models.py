class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0


    def set_position(self, position):
        self.position = position

    def __str__(self):
        return f"{self.name} is at position {self.position}"


class Snake:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail


class Ladder:
    def __init__(self, start, end):
        self.start = start
        self.end = end
