# File: Triangle.py

# Description: A basic 2D Triangle class

# Student Name:

# Student UT EID:

# Course Name: CS 313E

# Unique Number: 86610

import sys
import math

TOL = 0.01

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
      self.x = x
      self.y = y


  # get the distance to another Point object
  def dist (self, other):
      
      return  math.hypot (self.x - other.x, self.y - other.y)


class Triangle (object):
    # constructor
    def __init__(self, PointA, PointB, PointC):
        self.pointA = PointA
        self.pointB = PointB 
        self.pointC = PointC


    # check congruence of Triangles with equality
    # returns True or False (bolean)
    def __eq__(self, other):
        my_sides = [self.pointA.dist(self.pointB), self.pointA.dist(self.pointC), 
self.pointB.dist(self.pointC)]
        my_sides.sort()
        other_sides = [other.pointA.dist(other.pointB), 
other.pointA.dist(other.pointC), other.pointB.dist(other.pointC)]
        other_sides.sort()
        if my_sides == other_sides:
            return True
        else:
            return False


    # returns whether or not the triangle is valid
    # returns True or False (bolean)
    def is_triangle(self):
       A_to_B = self.pointA.dist(self.pointB)
       B_to_C = self.pointB.dist(self.pointC)
       A_to_C = self.pointA.dist(self.pointC)
      # the 3 points do not make a valid triangle if they fall along a line
       if A_to_B == (B_to_C + A_to_C):
           return False
       elif B_to_C == (A_to_B + A_to_C):
           return False
       elif A_to_C == (A_to_B + B_to_C):
           return False
       else:
           return True

    # return the area of the triangle:
    def area(self):
        tmp = self.pointA.x * (self.pointB.y - self.pointC.y)
        tmp += self.pointB.x * (self.pointC.y - self.pointA.y)
        tmp += self.pointC.x * (self.pointA.y - self.pointB.y)
        tmp = abs(tmp/2)
        return tmp


######################################################
# The code below is filled out for you, DO NOT EDIT. #
######################################################

# takes a string of coordinates and changes it to a list of Points
def get_points(coords_str):
    coords = [float(c) for c in coords_str.split(" ")]
    return [Point(c[0], c[1]) for c in zip(*[iter(coords)]*2)]

def main():
    # read the two triangles
    pointsA = get_points(sys.stdin.readline().strip())
    pointsB = get_points(sys.stdin.readline().strip())

    triangleA = Triangle(pointsA[0], pointsA[1], pointsA[2])
    triangleB = Triangle(pointsB[0], pointsB[1], pointsB[2])

    # Print final output
    print(triangleA.area())
    print(triangleB.area())
    print(triangleA.is_triangle())
    print(triangleB.is_triangle())
    print(triangleA == triangleB)

if __name__ == "__main__":
    main()
