# Project 3 - Calcudoku
# 
# Name: Nicholas Baggett
# Instructor: Hatalsky

def check_valid(puzzle, cages):
   checkCages = check_cages_valid(puzzle, cages)
   checkCol = check_columns_valid(puzzle)
   checkRow = check_rows_valid(puzzle)
   if (checkRow == True) and (checkCol == True) and (checkCages == True):
      return True
   else:
      return False
      
def check_cages_valid(puzzle, cages):
   def convertIndex(i, puzzle):
      if i == 0:
         i = puzzle[0][0]
         return i
      if i == 1:
         i = puzzle[0][1]
         return i
      if i == 2:
         i = puzzle[0][2]
         return i
      if i == 3:
         i = puzzle[0][3]
         return i
      if i == 4:
         i = puzzle[0][4]
         return i
      if i == 5:
         i = puzzle[1][0]
         return i
      if i == 6:
         i = puzzle[1][1]
         return i
      if i == 7:
         i = puzzle[1][2]
         return i
      if i == 8:
         i = puzzle[1][3]
         return i
      if i == 9:
         i = puzzle[1][4]
         return i
      if i == 10:
         i = puzzle[2][0]
         return i
      if i == 11:
         i = puzzle[2][1]
         return i
      if i == 12:
         i = puzzle[2][2]
         return i
      if i == 13:
         i = puzzle[2][3]
         return i
      if i == 14:
         i = puzzle[2][4]
         return i
      if i == 15:
         i = puzzle[3][0]
         return i
      if i == 16:
         i = puzzle[3][1]
         return i
      if i == 17:
         i = puzzle[3][2]
         return i
      if i == 18:
         i = puzzle[3][3]
         return i
      if i == 19:
         i = puzzle[3][4]
         return i
      if i == 20:
         i = puzzle[4][0]
         return i
      if i == 21:
         i = puzzle[4][1]
         return i
      if i == 22:
         i = puzzle[4][2]
         return i
      if i == 23:
         i = puzzle[4][3]
         return i
      if i == 24:
         i = puzzle[4][4]
         return i
   indexes = []
   x = 1
   while x < len(cages):
      indexes.append(cages[x][2:])
      x += 1
   
   valueInCage = []
   for list in indexes:
      smalist = []
      for i in list:
         cellVal = convertIndex(i, puzzle)
         smalist.append(cellVal)
      valueInCage.append(smalist)
   
   cageSums = []
   for list in valueInCage:
      sum = 0
      for i in list:
         sum += i
      cageSums.append(sum)
   
   isFalse = 0
   isFull = []
   for list in valueInCage:
      x = 0
      torf = None
      for val in list:
         if val == 0:
            torf = False
            break
         elif val > 0:
            torf = True
      if torf == False:
         isFull.append(False)
      if torf == True:
         isFull.append(True)
   
   for val in cageSums:
      x = 0
      isFalse = 0
      while x < len(cages) - 1:
         if isFull[x] == False:
            if cageSums[x] >= cages[x + 1][0]:
               isFalse = 1
               break
         elif isFull[x] == True:
            if cageSums[x] < cages[x + 1][0] or cageSums[x] > cages[x + 1][0]:
               isFalse = 1
               break
         x += 1
      if isFalse == 1:
         break
      
   if isFalse == 0:
      return True
   if isFalse == 1:
      return False
      
def check_columns_valid(puzzle):
   isFalse = 0
   x = 0
   while x < 5:
      one = 0
      two = 0
      three = 0
      four = 0 
      five = 0    
      column = ([i[x] for i in puzzle])
      for val in column:
         if val == 1:
            one += 1
         if val == 2: 
            two += 1
         if val == 3:
            three += 1
         if val == 4:
            four += 1
         if val == 5:
            five += 1
      x += 1
      if (one > 1 or two > 1 or three > 1 or four > 1 or five > 1):
         isFalse += 1
         break
   if isFalse > 0:
      return False
   elif isFalse == 0:
      return True
         
def check_rows_valid(puzzle):
   isFalse = 0
   for row in puzzle:
      one = 0
      two = 0
      three = 0
      four = 0 
      five = 0
      for val in row:
         if val == 1:
            one += 1
         if val == 2: 
            two += 1
         if val == 3:
            three += 1
         if val == 4:
            four += 1
         if val == 5:
            five += 1
      if (one > 1 or two > 1 or three > 1 or four > 1 or five > 1):
         isFalse += 1
         break
   if isFalse > 0:
      return False
   elif isFalse == 0:
      return True
      
def get_cages():
   cageNum = int(input("Number of cages: "))
   cageList = [cageNum]
   counter = 0
   cages = []
   cages.append(cageList)
   while counter < cageNum:
      subCages = []
      theirCage = input("Cage number %i: "%counter).split()
      theirCage = [int(i) for i in theirCage]
      cages.append(theirCage)
      counter += 1
   return cages   
   