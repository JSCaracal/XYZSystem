import numpy as np
import math as m
class Point3d():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.mat = np.array([[self.x],[self.y],[self.z]])

class Vector(Point3d):
    def __init__(self,x,y,z):
        super().__init__(x,y,z)
    def Magnitude(self):
        return m.sqrt(self.x**2+self.y**2+self.z**2)
    def UnitVector(self):
        uX = 1/self.Magnitude()
        return np.multiply(uX,self.mat)
    def Length(self):
        return m.sqrt(np.matmul(np.transpose(self.mat),self.mat))
    
        
v = Vector(3,4,2)
print(v.Length())

