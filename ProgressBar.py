class ProgressBar:
    def __init__(self, length, fill = '#',unfill = '-'):
        self.length = length
        self.fill = fill
        self.unfill = unfill

        self.outputs = []

    def __call__(self, progress):
        _fill = int(progress*self.length)
        _unfill = self.length - _fill


        bar = _fill*self.fill + _unfill*self.unfill
        

        return bar


if __name__ == "__main__":
    a = ProgressBar(100)
    print(a(1/10))
    print(a(0))
    print(a(0.1))
    print(a(0.01))
    

