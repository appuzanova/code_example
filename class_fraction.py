import sys


class Fraction:
    def __init__(self, a = 0, b = 0):
        if type(a) == type(self):
            self.a, self.b = a.a, a.b
        elif type(a) == str:
            if a.find(' ') != -1:
                self.a, self.b = map(int, a.split())
            elif a.find('/') != -1:
                self.a, self.b = map(int, a.split('/'))
            else:
                self.a, self.b = int(a), 1
        elif type(a) == int:
            if b == 0:
                self.a, self.b = a, 1
            else:
                self.a, self.b = a, b
        self.reduce()
        
    def __int__(self):
        return self.a // self.b
    
    def __float__(self):
        return self.a / self.b
    
    def __round__(self, digits = 0):
        return round(self.a / self.b, digits)
                
    def __str__(self):
        if self.b != 1:
            return str(self.a) + '/' + str(self.b)
        else:
            return str(self.a)
        
    def reduce(self):
        if self.b < 0:
            self.a *= -1
            self.b *= -1
        Gcd = gcd(self.a, self.b)
        self.a, self.b = self.a // Gcd, self.b // Gcd


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


exec(sys.stdin.read())