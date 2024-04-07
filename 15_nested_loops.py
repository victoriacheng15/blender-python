import bpy

count = 10

for i in range(count):
  for j in range(i):
    x = i * 3
    y = j * 3
    bpy.ops.mesh.primitive_cube_add(location=(x,y,0))


# excerise 1
# for i in range(count):
#   for j in range(count):
#     x = i * 3
#     z = j * 3
#     bpy.ops.mesh.primitive_cube_add(location=(x,0,z))


# excerise 2
# for i in range(count):
#   for j in range(count):
#     for k in range(count):
#         x = i * 3
#         y = j * 3
#         z = k * 3
#         if k >= count / 2:
#             bpy.ops.mesh.primitive_cube_add(location=(x,y,z))
#         else:
#             bpy.ops.mesh.primitive_ico_sphere_add(location=(x,y,z))
