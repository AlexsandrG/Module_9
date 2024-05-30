class EvenNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.count = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > self.end:
            raise StopIteration
        else:
            num = self.count
            self.count += 2
            return num


en = EvenNumbers(10, 25)
for i in en:
    print(i)
