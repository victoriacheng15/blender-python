import bpy
import random

current_location = -20

# excerise 1
for i in range(20):
  current_location += 2
  if current_location < 0:
    bpy.ops.mesh.primitive_cube_add(location=(0,0,current_location))
  else:
    bpy.ops.mesh.primitive_ico_sphere_add(location=(0,0,current_location))

# excerise 2
# for i in range(20):
#   current_location += 2
#   if random.randint(0,1):
#     bpy.ops.mesh.primitive_cube_add(location=(current_location,current_location,current_location))
#   else:
#     bpy.ops.mesh.primitive_ico_sphere_add(location=(current_location,current_location,current_location))