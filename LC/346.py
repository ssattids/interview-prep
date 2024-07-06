class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.values = []

    def average(self):
        return sum(self.values)/len(self.values)

    def next(self, val: int) -> float:
        if len(self.values) < self.size:
            self.values.append(val)
            return self.average()
        elif len(self.values) == self.size:
            self.values.pop(0)
            self.values.append(val)
            return self.average()