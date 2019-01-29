/* Nicholas Baggett */

/* This is a detab program. It removes tabs and replaces them with the 
appropriate amount of spaces. */

#include <stdio.h>
#define TABSPC 8

int main(int argc, char *argv[])
{
   int dex, c, numspc;

   dex = 0; 
   /* dex is the index on a given line, 
   0 is the first character on a line and so on */

   while((c = getchar()) != EOF)
   {
      if(c == '\t')
      {
         numspc = TABSPC - (dex % TABSPC); 
         /* this formula calculates the number of spaces 
         needed for a given tab */

         while(numspc > 0)
         {
            putchar(' ');
            dex++;
            numspc--;
         }
      }

      else if(c == '\n')
      {
         putchar(c);
         dex = 0; 
         /* need to set the index back to zero 
         once a new line is detected */ 
      }

      else if(c == '\b' && dex > 0)
      {
         putchar(c);
         dex--;
      }
      else
      {
         putchar(c);
         dex++;
      }
   }
   return 0;
}
