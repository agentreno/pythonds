# Fraction type
#
# Numerator can be any integer
# Denominator must be an integer greater than 0
# Negative fractions will have a negative numerator
# Must support add/subtract/multiple/divide
# Must display fraction in slash form with lowest terms

class Fraction:

   def __init__(self, top, bottom):
      if isinstance(top, int) and isinstance(bottom, int):
         common = self.gcd(top, bottom)
         self.num = top // common
         self.den = bottom // common
      else:
         raise TypeError("Numerator and denominator must both be integers")

   def __str__(self):
      return str(self.num) + "/" + str(self.den)

   def __repr__(self):
      return str(self.num) + "/" + str(self.den)

   def __eq__(self, other):
      firstnum = self.num * other.den
      secondnum = other.num * self.den

      return firstnum == secondnum

   def __ne__(self, other):
      firstnum = self.num * other.den
      secondnum = other.num * self.den

      return firstnum != secondnum

   def __lt__(self, other):
      firstnum = self.num * other.den
      secondnum = other.num * self.den

      return firstnum < secondnum

   def __le__(self, other):
      firstnum = self.num * other.den
      secondnum = other.num * self.den

      return firstnum <= secondnum

   def __gt__(self, other):
      firstnum = self.num * other.den
      secondnum = other.num * self.den

      return firstnum > secondnum

   def __ge__(self, other):
      firstnum = self.num * other.den
      secondnum = other.num * self.den

      return firstnum >= secondnum

   def gcd(self, m, n):
      while m % n != 0:
         oldm = m
         oldn = n
         m = oldn
         n = oldm % oldn
      return n

   def __add__(self, other):
      if isinstance(other, Fraction):
         newnum = (self.num * other.den) + (self.den * other.num)
         newden = self.den * other.den
      elif isinstance(other, int):
         otherfrac = Fraction(other, 1)
         return self.__add__(otherfrac)
      else:
         raise TypeError("Can only add to other fractions or integers")

      return Fraction(newnum, newden)

   def __radd__(self, other):
      if isinstance(other, int):
         otherfrac = Fraction(other, 1)
         return self.__add__(otherfrac)
      else:
         raise TypeError("Can only add to other fractions or integers")

   def __iadd__(self, other):
      # TODO: Implement
      pass

   def __sub__(self, otherfraction):
      newnum = (self.num * otherfraction.den) - (self.den * otherfraction.num)
      newden = self.den * otherfraction.den
      common = self.gcd(newnum, newden)

      return Fraction(newnum // common, newden // common)

   def __mul__(self, otherfraction):
      newnum = self.num * otherfraction.num
      newden = self.den * otherfraction.den
      common = self.gcd(newnum, newden)

      return Fraction(newnum // common, newden // common)

   def __truediv__(self, otherfraction):
      newnum = self.num * otherfraction.den
      newden = self.den * otherfraction.num
      common = self.gcd(newnum, newden)

      return Fraction(newnum // common, newden // common)

   def getNum(self):
      return self.num

   def getDen(self):
      return self.den
