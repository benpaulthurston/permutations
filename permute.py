import math
class permute:
    n = 0
    count = 0
    def __init__(self, n):
        self.n = n
    def next(self):
        a = []
        num = self.count
        for i in range(self.n-1, 0, -1):
            f = math.factorial(i)
            c = math.floor(num / f)
            a.append(c+1)
            num = num - c*f
        self.count = self.count+1
        a.append(1)
        return self.fill(a)
    def fill(self, a):
        p = [0]*self.n
        v = self.n
        for i in range(0, len(a)):
            zeroes = 0
            for j in range(0, len(p)):
                if p[j] == 0:
                    zeroes +=1
                if zeroes == a[i]:
                    p[j] = v
                    v -= 1
                    break
        return p
p = permute(5)
for i in range(0, math.factorial(5)):
    print(p.next())
