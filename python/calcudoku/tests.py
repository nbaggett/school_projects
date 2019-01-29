import unittest
from solverFuncs import *

class TestCases(unittest.TestCase):
      
   def test_check_rows0(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([4, 0, 0, 0, 0])
      self.assertTrue(check_rows_valid(puzzle))
      
   def test_check_rows1(self):
      puzzle = []
      puzzle.append([5, 2, 1, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 3, 1, 2])
      puzzle.append([0, 0, 1, 1, 0])
      self.assertFalse(check_rows_valid(puzzle))
      
   def test_check_col0(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([3, 2, 0, 5, 0])
      self.assertFalse(check_columns_valid(puzzle))
      
   def test_check_col1(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([4, 0, 0, 0, 0])
      self.assertTrue(check_columns_valid(puzzle))
   
   def test_check_cages0(self):
      puzzle = []
      puzzle.append([3, 5, 2, 1, 4])
      puzzle.append([5, 1, 3, 4, 2])
      puzzle.append([2, 4, 1, 5, 3])
      puzzle.append([1, 2, 4, 3, 5])
      puzzle.append([4, 3, 5, 2, 1])
      cages = []
      cages.append([9])
      cages.append([9, 3, 0, 5, 6])
      cages.append([7, 2, 1, 2])
      cages.append([10, 3, 3, 8, 13])
      cages.append([14, 4, 4, 9, 14, 19])
      cages.append([3, 1, 7])
      cages.append([8, 3, 10, 11, 16])
      cages.append([13, 4, 12, 17, 21, 22])
      cages.append([5, 2, 15, 20])
      cages.append([6, 3, 18, 23, 24])
      self.assertTrue(check_cages_valid(puzzle, cages))
      
   def test_check_cages1(self):
      puzzle = []
      puzzle.append([4, 5, 2, 1, 4])
      puzzle.append([5, 1, 3, 4, 2])
      puzzle.append([2, 4, 1, 5, 3])
      puzzle.append([1, 2, 4, 3, 5])
      puzzle.append([4, 3, 5, 2, 1])
      cages = []
      cages.append([9])
      cages.append([9, 3, 0, 5, 6])
      cages.append([7, 2, 1, 2])
      cages.append([10, 3, 3, 8, 13])
      cages.append([14, 4, 4, 9, 14, 19])
      cages.append([3, 1, 7])
      cages.append([8, 3, 10, 11, 16])
      cages.append([13, 4, 12, 17, 21, 22])
      cages.append([5, 2, 15, 20])
      cages.append([6, 3, 18, 23, 24])
      self.assertFalse(check_cages_valid(puzzle, cages))
      
   def test_check_cages2(self):
      puzzle = []
      puzzle.append([0, 5, 2, 1, 4])
      puzzle.append([5, 1, 3, 4, 2])
      puzzle.append([2, 4, 0, 5, 3])
      puzzle.append([1, 2, 4, 3, 5])
      puzzle.append([4, 3, 5, 2, 0])
      cages = []
      cages.append([9])
      cages.append([9, 3, 0, 5, 6])
      cages.append([7, 2, 1, 2])
      cages.append([10, 3, 3, 8, 13])
      cages.append([14, 4, 4, 9, 14, 19])
      cages.append([3, 1, 7])
      cages.append([8, 3, 10, 11, 16])
      cages.append([13, 4, 12, 17, 21, 22])
      cages.append([5, 2, 15, 20])
      cages.append([6, 3, 18, 23, 24])
      self.assertTrue(check_cages_valid(puzzle, cages))
      
   def test_check_cages3(self):
      puzzle = []
      puzzle.append([0, 5, 2, 1, 4])
      puzzle.append([5, 4, 3, 4, 2])
      puzzle.append([2, 4, 1, 5, 3])
      puzzle.append([1, 2, 4, 3, 5])
      puzzle.append([4, 3, 5, 0, 3])
      cages = []
      cages.append([9])
      cages.append([9, 3, 0, 5, 6])
      cages.append([7, 2, 1, 2])
      cages.append([10, 3, 3, 8, 13])
      cages.append([14, 4, 4, 9, 14, 19])
      cages.append([3, 1, 7])
      cages.append([8, 3, 10, 11, 16])
      cages.append([13, 4, 12, 17, 21, 22])
      cages.append([5, 2, 15, 20])
      cages.append([6, 3, 18, 23, 24])
      self.assertFalse(check_cages_valid(puzzle, cages))
      
   def test_check_valid0(self):
      puzzle = []
      puzzle.append([3, 5, 2, 1, 4])
      puzzle.append([5, 1, 3, 4, 2])
      puzzle.append([2, 4, 1, 5, 3])
      puzzle.append([1, 2, 4, 3, 5])
      puzzle.append([4, 3, 5, 2, 1])
      cages = []
      cages.append([9])
      cages.append([9, 3, 0, 5, 6])
      cages.append([7, 2, 1, 2])
      cages.append([10, 3, 3, 8, 13])
      cages.append([14, 4, 4, 9, 14, 19])
      cages.append([3, 1, 7])
      cages.append([8, 3, 10, 11, 16])
      cages.append([13, 4, 12, 17, 21, 22])
      cages.append([5, 2, 15, 20])
      cages.append([6, 3, 18, 23, 24])
      self.assertTrue(check_valid(puzzle, cages))
      
   def test_check_valid1(self):
      puzzle = []
      puzzle.append([3, 5, 2, 1, 4])
      puzzle.append([5, 5, 3, 4, 2])
      puzzle.append([2, 4, 1, 5, 3])
      puzzle.append([1, 2, 4, 3, 5])
      puzzle.append([4, 3, 3, 2, 1])
      cages = []
      cages.append([9])
      cages.append([9, 3, 0, 5, 6])
      cages.append([7, 2, 1, 2])
      cages.append([10, 3, 3, 8, 13])
      cages.append([14, 4, 4, 9, 14, 19])
      cages.append([3, 1, 7])
      cages.append([8, 3, 10, 11, 16])
      cages.append([13, 4, 12, 17, 21, 22])
      cages.append([5, 2, 15, 20])
      cages.append([6, 3, 18, 23, 24])
      self.assertFalse(check_valid(puzzle, cages))
      
   def test_check_valid2(self):
      puzzle = [[0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0]]
      cages = []
      cages.append([9])
      cages.append([9, 3, 0, 5, 6])
      cages.append([7, 2, 1, 2])
      cages.append([10, 3, 3, 8, 13])
      cages.append([14, 4, 4, 9, 14, 19])
      cages.append([3, 1, 7])
      cages.append([8, 3, 10, 11, 16])
      cages.append([13, 4, 12, 17, 21, 22])
      cages.append([5, 2, 15, 20])
      cages.append([6, 3, 18, 23, 24])
      self.assertTrue(check_valid(puzzle, cages))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

