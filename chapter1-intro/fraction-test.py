import unittest
from fraction import Fraction

class FractionTest(unittest.TestCase):
   def test_fractions_eq_comparison(self):
      f1 = Fraction(1, 2)
      f2 = Fraction(1, 2)
      isEqual = (f1 == f2)
      
      self.assertEqual(isEqual, True)

   def test_fractions_eq_comparison_with_negatives(self):
      f1 = Fraction(-1, 2)
      f2 = Fraction(1, -2)
      isEqual = (f1 == f2)

      self.assertEqual(isEqual, True)

   def test_fractions_ne_comparison(self):
      f1 = Fraction(1, 2)
      f2 = Fraction(1, 3)
      isEqual = (f1 == f2)

      self.assertEqual(isEqual, False)

   def test_fractions_lt_comparison(self):
      f1 = Fraction(1, 3)
      f2 = Fraction(1, 2)
      isLessThan = (f1 < f2)

      self.assertEqual(isLessThan, True)

   def test_fractions_lt_comparison_with_negatives(self):
      f1 = Fraction(1, -2)
      f2 = Fraction(-1, 3)
      isLessThan = (f1 < f2)

      self.assertEqual(isLessThan, True)

   def test_fractions_le_comparison(self):
      f1 = Fraction(1, 3)
      f2 = Fraction(1, 2)
      f3 = Fraction(1, 2)
      isLessThan = (f1 <= f2)
      isEqualTo = (f2 <= f3)

      self.assertEqual(isLessThan, True)
      self.assertEqual(isEqualTo, True)

   def test_fractions_gt_comparison(self):
      f1 = Fraction(1, 2)
      f2 = Fraction(1, 3)
      isGreaterThan = (f1 > f2)

      self.assertEqual(isGreaterThan, True)

   def test_fractions_ge_comparison(self):
      f1 = Fraction(1, 2)
      f2 = Fraction(1, 2)
      f3 = Fraction(1, 3)
      isGreaterThan = (f1 >= f3)
      isEqualTo = (f1 >= f2)

      self.assertEqual(isGreaterThan, True)
      self.assertEqual(isEqualTo, True)

   def test_add_two_fractions(self):
      f1 = Fraction(1, 3)
      f2 = Fraction(1, 3)
      f3 = f1 + f2

      self.assertEqual(f3.num, 2)
      self.assertEqual(f3.den, 3)

   def test_sub_two_fractions(self):
      f1 = Fraction(1, 2)
      f2 = Fraction(1, 3)
      f3 = f1 - f2

      self.assertEqual(f3.num, 1)
      self.assertEqual(f3.den, 6)

   def test_mul_two_fractions(self):
      f1 = Fraction(2, 3)
      f2 = Fraction(1, 2)
      f3 = f1 * f2

      self.assertEqual(f3.num, 1)
      self.assertEqual(f3.den, 3)

   def test_div_two_fractions(self):
      f1 = Fraction(1, 3)
      f2 = Fraction(1, 2)
      f3 = f1 / f2

      self.assertEqual(f3.num, 2)
      self.assertEqual(f3.den, 3)

   def test_construct_fraction_without_integer_raises_typeerror(self):
      with self.assertRaises(TypeError):
         f1 = Fraction(1.0, 2)

      with self.assertRaises(TypeError):
         f2 = Fraction(1, 2.0)

      with self.assertRaises(TypeError):
         f3 = Fraction(1.0, 2.0)

if __name__ == '__main__':
   unittest.main()
