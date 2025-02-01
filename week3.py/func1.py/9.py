import math
def volumesph(radius):
    Volume = ( 4/3 * math.pi *(radius * radius * radius))
    return Volume 
    
radius=float(input(" Enter a radius of the sphere to find volume:") )
print(volumesph(radius))