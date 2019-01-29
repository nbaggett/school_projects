# Project 3 - Calcudoku
# 
# Name: Nicholas Baggett
# Instructor: Hatalsky

from solverFuncs import *
def main():
   puzzle = [[0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0]]
   backtracks = [0]
   checks = [0]
   cages = get_cages()
   print()
   print("---Solution---")
   print()
   row = 0
   col = 0
   checks = 0
   backtracks = 0
   while row < 5:
      puzzle[row][col] += 1
      if check_valid(puzzle, cages) == True:
         checks += 1
         col += 1
         if col > 4:
            col = 0
            row += 1
      else: 
         checks += 1
         if puzzle[row][col] == 5:
            while puzzle[row][col] == 5:
               puzzle[row][col] = 0
               col -= 1
               backtracks += 1
               if col < 0:
                  col = 4
                  row -= 1
   for row in puzzle:
      for val in row:
         print(val, end = " ")
      print()
   print()
   print('checks:', checks, 'backtracks:', backtracks)
if __name__ == '__main__':
   main()

