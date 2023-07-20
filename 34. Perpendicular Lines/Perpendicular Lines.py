# import sympy and Point, Line
from sympy import Point, Line
  
p1, p2, p3 = Point(0, 0), Point(2, 3), Point(-2, 2)
  
l1 = Line(p1, p2)
  
# using perpendicular_line() method
l2 = l1.perpendicular_line(p3)
  
# checking l2 is perpendicular to l1 using is_perpendicular() method
isPerpendicular = l1.is_perpendicular(l2)
  
print(isPerpendicular)
