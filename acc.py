class Acc:

    def __init__(self, initNum):
        self.initNum = initNum

    def add(self, plusNum):
        self.initNum += plusNum
        return initNum

# Examples:
# >>> foo = Acc(0)
# >>> foo.add(3)
# 3
# >>> foo.add(4)
# 7
# >>> foo.add(6)
# 13