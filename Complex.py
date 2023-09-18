#!/usr/bin/python3

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        pass
    
    def __add__(self, no):
        new_real = self.real + no.real
        new_imaginary = self.imaginary + no.imaginary
        return Complex(new_real, new_imaginary)
    
    def __sub__(self, no):
        new_real = self.real - no.real
        new_imaginary = self.imaginary - no.imaginary
        return Complex(new_real, new_imaginary)
            
    def __mul__(self, no):
        """
        When you multiply instances of the ComplexNumber class, 
        the __mul__ method calculates the result based on the rules 
        for complex number multiplication: 
        (a + bj) * (c + dj) = (a*c - b*d) + (a*d + b*c)j.
        
        """
        new_real = self.real * no.real - self.imaginary * no.imaginary
        new_imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(new_real, new_imaginary)
    
    def __truediv__(self, no):
        """
        When you divide instances of the ComplexNumber class, 
        the __truediv__ method calculates the result based on the rules 
        for complex number division: 
        (a + bj) / (c + dj) = (a*c + b*d) / (c^2 + d^2) + (b*c - a*d) / (c^2 + d^2)j.
        """
        denominator = no.real ** 2 + no.imaginary ** 2
        new_real = (self.real * no.real + self.imaginary * no.imaginary) / denominator
        new_imaginary = (self.imaginary * no.real - self.real * no.imaginary) / denominator 
        return Complex(new_real, new_imaginary)
    
    def mod(self):
        real_value = (self.real ** 2 + self.imaginary ** 2) ** 0.5
        return Complex(real_value, 0)

    
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
    