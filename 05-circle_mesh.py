import bpy
import math
import pprint


vert_count = 32 
# can write math.tau instead of pi
angle_step = 2 * math.pi / vert_count
# for spiral shape
# z_step = 0.1
# increase size of circle
radius = 1

vert_coordinates = list()

for i in range(1, vert_count + 1):
    current_angle = i * angle_step

    x = radius * math.cos(current_angle)
    y = radius * math.sin(current_angle)

    bpy.ops.mesh.primitive_ico_sphere_add(radius=0.1, location=(x, y, 0))
    
    vert_coordinates.append((x,y,0))
    
pprint.pprint(vert_coordinates)
