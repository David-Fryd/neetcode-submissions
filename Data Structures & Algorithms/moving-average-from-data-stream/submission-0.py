class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.num_added = 0
        self.history = [None] * size

    def next(self, val: int) -> float:
        if self.num_added >= self.size:
            # need to shift window
            self.history = self.history[1:]
            self.history.append(val)
        else:
            # add to existing window
            self.history[self.num_added] = val
            self.num_added += 1

        avg = 0
        for i in range(self.num_added):
            avg += self.history[i]
        avg /= self.num_added

        return avg


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
