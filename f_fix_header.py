####slice out the incorrect header data 
from d_GL_gather_stats import headerstats



print(headerstats[0])
# headerstatsfinal=+TriangleMonth+
# headerstatsfinal.append()
# print(headerstatsfinal)
from c_capture_triangle_months import TriangleMonth


TriangleMonth.insert(0,headerstats[0])  ####
print(TriangleMonth)
headerstatsfinal=TriangleMonth