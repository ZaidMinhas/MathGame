class ProgressBar:
    def __init__(self, length, correct = '#', wrong = "X" ,unfill = '-'):
        self.length = length
        self.correct = correct
        self.wrong = wrong
        self.unfill = unfill

        self.outputs = []

    def __call__(self, output):
        self.outputs.append(output)
        progress_list = [self.correct if i else self.wrong for i in self.outputs]
        progress = " ".join(progress_list) + " "
        progress += " ".join(list((self.length-len(progress_list))*self.unfill))
        

        return progress


if __name__ == "__main__":
    a = ProgressBar(10)
    print(a(1))
    print(a(0))
    print(a(1))

