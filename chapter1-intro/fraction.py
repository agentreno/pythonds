# Fraction type
#
# Numerator can be any integer
# Denominator must be an integer greater than 0
# Negative fractions will have a negative numerator
# Must support add/subtract/multiple/divide
# Must display fraction in slash form with lowest terms

class Fraction:

   def __init__(self, top, bottom):
      self.num = top
      self.den = bottom

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

   def __add__(self, otherfraction):
      newnum = (self.num * otherfraction.den) + (self.den * otherfraction.num)
      newden = self.den * otherfraction.den
      common = self.gcd(newnum, newden)

      return Fraction(newnum // common, newden // common)

   def __sub__(self, otherfraction):
      newnum = (self.num * otherfraction.den) - (self.den * otherfraction.num)
      newden = self.den * otherfraction.den
      common = self.gcd(newnum, newden)

      return Fraction(newnum // common, newden // common)

   def __mul__(self, otherfraction):
      pass

   def __div__(self, otherfraction):
      pass
