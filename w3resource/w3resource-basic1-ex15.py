from math import pi

def calculateSphereVolume(radius):
     return (4/3) * pi * radius * radius * radius
    

radius = input("Enter sphere radius: ")
volume = calculateSphereVolume(float(radius))
print(volume)