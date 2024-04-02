import bpy
import random


left = random.randint(0, 10)
right = random.randint(0,10)

if left >= 5:
  bpy.ops.mesh.primitive_monkey_add()
else:
  bpy.ops.mesh.primitive_torus_add()
