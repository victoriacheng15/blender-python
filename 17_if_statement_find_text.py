import bpy
import math


location_offset = 3

for i in range(10):
    bpy.ops.mesh.primitive_cube_add(location=(i * location_offset, 0, 0))

for i in range(10):
    bpy.ops.mesh.primitive_ico_sphere_add(
        location=(i * location_offset, 0, location_offset)
    )

for i in range(10):
    bpy.ops.mesh.primitive_monkey_add(
        location=(i * location_offset, 0, location_offset * 2)
    )
       

# could use enumerate() to get index but keep in mind, it is a index based on the entire list
for index, obj in enumerate(bpy.data.objects):
    if "Cub" in obj.name:
        obj.name = f"obj.cube.{index}"
        obj.data.name = f"mesh.cube.{index}"
        if index > 6:
            obj.rotation_euler.z = math.radians(45)

for index, obj in enumerate(bpy.data.objects):
    if "Ico" in obj.name:
        obj.name = f"obj.ico.{index}"
        obj.data.name = f"mesh.ico.{index}"
        if index > 6:
            obj.location.z*= 4
        
for index, obj in enumerate(bpy.data.objects):
    if "Suz" in obj.name:
        obj.name = f"obj.monkey.{index}"
        obj.data.name = f"mesh.monkey.{index}"
        if index > 27:
            obj.scale *= 0.5