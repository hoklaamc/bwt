import sys

from_file = len(sys.argv) == 2

def concat_and_sort(col, char_array):
  i = 0
  # Concat
  while i < len(col):
    char_array[i] = col[i] + char_array[i]
    i = i + 1
  # Sort
  char_array.sort()

def init_char_array(col):
  char_array = []
  for char in col:
    char_array.append(char)
  char_array.sort()
  return char_array

def dwt_decode(r, col):
  l = len(col)
  char_array = init_char_array(col)
  for i in range(l - 1):
    concat_and_sort(col, char_array)
  return char_array[r - 1]

if (from_file):
  filename = sys.argv[1]
  with open(filename) as file:
    content = file.readlines()
    content = [line.strip() for line in content]
    for i in range(0, len(content) - 1, 2):
      print(dwt_decode(int(content[i]), content[i+1]))
else:
  while(True):
    r = int(sys.stdin.readline())
    if (r == 0):
      exit()
    col = sys.stdin.readline().strip()
    print(dwt_decode(r, col))
