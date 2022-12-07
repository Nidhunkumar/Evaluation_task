'''Read a matrix dimension, and print the matrix filled with consecutive numbers starting from
one(1).
The first cell (0,0) must have the number 1.
The last cell (n,m) must have the value n x m (The largest number).
All others will be filled diagonally, left bottom to right top.
For example
Input:
3
4
Output:
1 3 6 9
2 5 8 11
4 7 10 12

Input
3
3

Output
1 3 6
2 5 8
4 7 9


'''
def solution(row,column):
  if row <= 0 or column <=0:
    print(f'matrix dimension  should be grater than Zero ')
  else:
    items = list(range(1, row*column+1))
    for i in range(0,len(items),row):
      result=list(items[i:i+row])
      print(result)

solution(3,3)
