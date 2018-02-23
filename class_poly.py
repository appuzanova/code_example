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
        
    def __lt__(self, other):
        if type(other) == int:
            return self.a < self.b * other        
        elif type(other) == float:
            return self.a / self.b < other
        else:
            return (self.a * other.b - other.a * self.b) < 0
    
    def __le__(self, other):
        if type(other) == int:
            return self.a <= self.b * other        
        elif type(other) == float:
            return self.a / self.b <= other       
        else:
            return (self.a * other.b - other.a * self.b) <= 0
        
    def __eq__(self, other):
        if type(other) == int:
            return self.a == self.b * other        
        elif type(other) == float:
            return self.a / self.b == other
        else:
            return self.a == other.a and self.b == other.b
    
    def __ne__(self, other):
        if type(other) == int:
            return self.a != self.b * other        
        elif type(other) == float:
            return self.a / self.b != other       
        else:
            return self.a * other.b != other.a * self.b
        
    def __gt__(self, other):
        if type(other) == int:
            return self.a > self.b * other         
        elif type(other) == float:
            return self.a / self.b > other        
        else:
            return (self.a * other.b - other.a * self.b) > 0
        
    def __ge__(self, other):
        if type(other) == int:
            return self.a >= self.b * other         
        elif type(other) == int or type(other) == float:
            return self.a / self.b >= other      
        else:
            return (self.a * other.b - other.a * self.b) >= 0    
     
    def __add__(self, other):
        if type(other) == int:
            return Fraction(self.a + self.b * other, self.b)
        elif type(other) == float:
            return self.a / self.b + other
        elif type(other) == Fraction:
            return Fraction(self.a * other.b + self.b * other.a, self.b * other.b)
        else:
            return NotImplemented
        
    def __radd__(self, other):
        return self + other
    
    def __iadd__(self, other):
        self = self + other
        return self
    
    def __mul__(self, other):
        if type(other) == int:
            return Fraction(self.a * other, self.b)
        elif type(other) == float:
            return (self.a / self.b) * other
        elif type(other) == Fraction:
            return Fraction(self.a * other.a, self.b * other.b)
        else:
            return NotImplemented        
    
    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self = self * other
        return self
    
    def __truediv__(self, other):
            if type(other) == int:
                return Fraction(self.a, self.b * other)
            elif type(other) == float:
                return self.a / self.b / other
            elif type(other) == Fraction:
                return Fraction(self.a * other.b, self.b * other.a)
            
    def __rtruediv__(self, other):
        if type(other) == int:
            return Fraction(self.b * other, self.a)
        elif type(other) == float:
            return other / (self.a / self.b)
        elif type(other) == Fraction:
            return Fraction(self.b * other.a, self.a * other.b)
    
    def __itruediv__(self, other):
        self = self / other
        return self
    
    def __pow__(self, other):
            if type(other) == int:
                self.reduce()
                if other >= 0:
                    return Fraction(pow(self.a, other), pow(self.b, other))
                else:
                    return Fraction(pow(self.b, -other), pow(self.a, -other))
            elif type(other) == float:
                return pow(self.a / self.b, other)
            elif type(other) == Fraction:
                return pow(self.a / self.b, other.a / other.b)
            
    def __rpow__(self, other):
        if type(other) == int or type(other) == float:
            return pow(other, self.a / self.b)
        elif type(other) == Fraction:
            return pow(other.a / other.b, self.a / self.b)     
    
    def __ipow__(self, other):
        self = self ** other
        return self
    
    def __sub__(self, other):
            if type(other) == int:
                return Fraction(self.a - self.b * other, self.b)
            elif type(other) == float:
                return self.a / self.b - other
            elif type(other) == Fraction:
                return Fraction(self.a * other.b - self.b * other.a, self.b * other.b)
            else:
                return NotImplemented            
            
    def __rsub__(self, other):
        if type(other) == int:
            return Fraction(other * self.b - self.a, self.b)
        elif type(other) == float:
            return other - self.a / self.b
        elif type(other) == Fraction:
            return Fraction(self.b * other.a - self.a * other.b, self.b * other.b)
    
    def __isub__(self, other):
        self = self - other
        return self    
                 
    def __str__(self):
        if self.b != 1 and self.a != 0:
            return str(self.a) + '/' + str(self.b)
        else:
            return str(self.a)
    
    def reduce(self):
        if self.b < 0:
            self.a *= -1
            self.b *= -1
        Gcd = gcd(self.a, self.b)
        self.a, self.b = self.a // Gcd, self.b // Gcd


class Poly():
    def __init__(self, k = 0):
        if type(k) == int or type(k) == float or type(k) == Fraction:
            self.k = [k]
        elif type(k) == list:
            self.k = k.copy()
        elif type(k) == tuple:
            self.k = list(k).copy()
        elif type(k) == str:
            self.k = []
            for elem in k.split():
                self.k.append(eval(elem))
        elif type(k) == Poly:
            self.k = k.k.copy()
                
    def __str__(self):
        Deg = [chr(8304), chr(185), chr(178), chr(179), chr(8308), chr(8309), chr(8310), chr(8311), chr(8312), chr(8313)]
        length = len(self.k)
        s = ''
        for i in range(length - 1, -1, -1):
            coeff = self.k[i]
            if coeff != 0 or (i == 0 and len(s) == 0):
                if len(s) == 0:
                    s += '-' * (coeff < 0)
                else:
                    s += ' + ' * (coeff > 0) + ' - ' * (coeff < 0)
                if type(coeff) == Fraction:
                    if coeff.b != 1:
                        s += '(' + str(abs(coeff.a)) + '/' + str(coeff.b) + ')'
                    elif abs(coeff.a) != 1 or (abs(coeff.a) == 1 and i == 0):
                        s += str(abs(coeff.a))
                elif type(coeff) == int and (abs(coeff) != 1 or (abs(coeff) == 1 and i == 0)):
                    s += str(abs(coeff))                
                elif type(coeff) == float:
                    if coeff == 0.0:
                        s += '0'
                    else:
                        s += str(abs(round(coeff, 3)))
                if i == 1:
                    s += 'x'
                elif i != 0:
                    s += 'x'
                    for k in range(len(str(i))):
                        s += Deg[int(str(i)[k])]
        return s
    
    def __add__(self, other):
        if type(other) == int or type(other) == float or type(other) == Fraction:
            coeffs = self.k.copy()
            coeffs[0] += other
            return Poly(coeffs)
        elif type(other) == Poly:
            coeffs1 = self.k.copy()
            coeffs2 = other.k.copy()
            if len(coeffs1) > len(coeffs2):
                coeffs1, coeffs2 = coeffs2, coeffs1
            for i in range(len(coeffs1)):
                coeffs2[i] = coeffs1[i] + coeffs2[i]
            return Poly(coeffs2)
        
    def __radd__(self, other):
        return self + other
    
    def __iadd__(self, other):
        if type(other) == int or type(other) == float or type(other) == Fraction:
            self.k[0] += other
            return self
        elif type(other) == Poly:
            length1, length2 = len(self.k), len(other.k)
            if length1 >= length2:
                for i in range(length2):
                    self.k[i] = self.k[i] + other.k[i]
                return self
            elif length2 > length1:
                for i in range(length1):
                    self.k[i] = other.k[i] + self.k[i]
                for i in range(length1, length2):
                    self.k.append(other.k[i])
                return self
    
    def __sub__(self, other):
        if type(other) == int or type(other) == float or type(other) == Fraction:
            coeffs = self.k.copy()
            coeffs[0] -= other
            return Poly(coeffs)
        elif type(other) == Poly:
            coeffs1, coeffs2 = self.k.copy(), other.k.copy()
            length1, length2 = len(coeffs1), len(coeffs2)
            if length1 >= length2:
                for i in range(length2):
                    coeffs1[i] = coeffs1[i] - coeffs2[i]
                return Poly(coeffs1)
            elif length2 > length1:
                for i in range(length1):
                    coeffs1[i] = coeffs1[i] - coeffs2[i]
                for i in range(length1, length2):
                    coeffs1.append(-1 * coeffs2[i])
                return Poly(coeffs1)
    
    def __rsub__(self, other):
        if type(other) == int or type(other) == float or type(other) == Fraction:
            coeffs = [-1 * self.k[i] for i in range(len(self.k))]
            coeffs[0] = other + coeffs[0]
            return Poly(coeffs)
        elif type(other) == Poly:
            coeffs1, coeffs2 = self.k.copy(), other.k.copy()
            length1, length2 = len(coeffs1), len(coeffs2)
            if length2 >= length1:
                for i in range(length1):
                    coeffs2[i] = coeffs2[i] - coeffs2[i]
                return Poly(coeffs2)
            elif length1 > length2:
                for i in range(length2):
                    coeffs2[i] = coeffs1[i] - coeffs2[i]
                for i in range(length2, length1):
                    coeffs2.append(-1 * coeffs1[i])
                return Poly(coeffs2)
            
    def __isub__(self, other):
        if type(other) == int or type(other) == float or type(other) == Fraction:
            self.k[0] -= other
            return self
        elif type(other) == Poly:
            length1, length2 = len(self.k), len(other.k)
            if length1 >= length2:
                for i in range(length2):
                    self.k[i] = self.k[i] - other.k[i]
                return self
            elif length2 > length1:
                for i in range(length1):
                    self.k[i] = self.k[i] - other.k[i]
                for i in range(length1, length2):
                    self.k.append(-1 * other.k[i])
                return self
            
    def __mul__(self, other):
        if type(other) == int or type(other) == float or type(other) == Fraction:
            coeffs = [other * self.k[i] for i in range(len(self.k))]
            return Poly(coeffs)
        elif type(other) == Poly:
            length1, length2 = len(self.k), len(other.k)
            coeffs = [0 for i in range(length1 + length2 - 1)]
            for i in range(length1):
                for j in range(length2):
                    coeffs[i + j] += self.k[i] * other.k[j]
            return Poly(coeffs)
        
    def __rmul__(self, other):
        return self * other         
        
    def __imul__(self, other):
        if type(other) == int or type(other) == float or type(other) == Fraction:
            self = [other * self.k[i] for i in range(len(self.k))]
            return self
        elif type(other) == Poly:
            length1, length2 = len(self.k), len(other.k)
            coeffs = [0 for i in range(length1 + length2)]
            for i in range(length1):
                for j in range(length2):
                    coeffs[i + j] += self.k[i] * other.k[j]
            self.k = coeffs
            return self
        
    def __pow__(self, other):
        Copy = Poly()
        Copy.k = self.k
        return Fastpow(Copy, other)
    
    def __ipow__(self, other):
        self.k = (self ** other).k
        return self
    
    def __len__(self):
        return len(self.k)
    
    def __getitem__(self, i):
        if len(self) <= i or i < 0:
            raise IndexError()
        else:
            return self.k[i]
    
    def __setitem__(self, i, val):
        if i < 0:
            raise IndexError()
        elif i >= len(self):
            for i in range(i - len(self)):
                self.k.append(0)
            self.k.append(val)
        else:
            self.k[i] = val
            
    def __or__(self, other):
        ans = 0
        for i in range(len(self.k) - 1, -1, -1):
            ans = other * ans + self.k[i]
        return ans  
    
    def __call__(self, x):
        return self | x         
            

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def Fastpow(x, n):
    res = Poly(1)
    while n:
        if (n & 1):
            res = res * x
        n = n >> 1
        if n:
            x = x * x
    return res


exec(sys.stdin.read())