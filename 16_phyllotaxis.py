import bpy
import random
import math

sphere_radius = 0.5

scale_fac = 1.0
angle = math.radians(random.uniform(137.0, 138.0))
#angle = math.radians(137.508)
count = 100


for n in range(count):
  current_angle = n * angle
  current_radius = scale_fac * math.sqrt(n)

  x = current_radius * math.cos(current_angle)
  y = current_radius * math.sin(current_angle)

  bpy.ops.mesh.primitive_ico_sphere_add(radius=sphere_radius, location=(x,y,0))
