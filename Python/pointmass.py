@@ This is a simple library of vector operations that I use sometimes when doing Linear Algebra homework as it serves as a
@@ great clarifier for certain concepts, especially in the area of vector spaces. 
@@ In the future, as I learn more about math and linear Alegebra, I intend to add more operations to this already useful library. 


import math

class PointMass:
    def __init__(self,a,b,c):
        self.x = a
        self.y = b
        self.mass = c

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getM(self):
        return self.mass

    def scale(self,k):
        self.x = self.x * k
        self.y = self.y * k

    def rotate(self, theta):
        self.rot_x = (self.x * math.cos(theta)) - (self.y * math.sin(theta))
        self.rot_y = (self.x * math.sin(theta)) - (self.y * math.cos(theta))
        self.x = self.rot_x
        self.y = self.rot_y


def secondMoment(obj_list):
    accum = 0
    for i in obj_list:
        accum = accum + (i.mass + (i.y**2))
    return accum
        
        
