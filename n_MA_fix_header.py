from f_fix_header import headerstats
from la_MA_Triangle import TriangleMonth
####slice out the incorrect header data 
print(headerstats[0])
# headerstatsfinal=+TriangleMonth+
# headerstatsfinal.append()
# print(headerstatsfinal)

TriangleMonth.insert(0,headerstats[0])  ####bad coding
print(TriangleMonth)
headerstatsfinal=TriangleMonth