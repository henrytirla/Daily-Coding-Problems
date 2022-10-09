"""Given a string and a number of lines k, print the string in zigzag form. In zigzag,
characters are printed out diagonally from top left to bottom right until reaching
the k th line, then back up to top right, and so on.

EG Thisisazigzag and k=4

 t       a        g
  h     s z     a
    i  i   i   z
      s      g



Solution Explanation Medium: https://henrytirla.medium.com/day-8-print-a-string-in-zigzag-form-in-k-rows-python-9ec5c05351cf
In case of any questiions leave a comment
"""

def printZigZag(s, k):
 space =""
 # base case
 if k == 0:
  return

 # base case
 if k == 1:
  print(s, end='')
  return

 # print first row
 for i in range(0, len(s), (k - 1) * 2):
  print(s[i], end='')


 # print middle rows
 for j in range(1, k - 1):

  down = True
  i = j

  while i < len(s):
   print("down", s[i], end='')
   if down:  # going down
    i += (k - j - 1) * 2

   else:  # going up
    i += (k - 1) * 2 - (k - j - 1) * 2


   down = not down  # switch direction

 # print last row
 for i in range(k - 1, len(s), (k - 1) * 2):
  print(s[i], end='')


if __name__ == '__main__':
 s = 'Thisisazigzag'
 k = 4

 printZigZag(s, k)