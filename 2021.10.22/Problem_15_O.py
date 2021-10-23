from math import *

Column = 20
Row = 20

Routes = factorial (Column + Row) / (factorial (Column) * factorial (Row))

print (int (Routes))