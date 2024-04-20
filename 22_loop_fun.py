import bpy
import math
import random


bpy.ops.mesh.primitive_cube_add()
obj = bpy.context.active_object
# x y z
obj.scale = (0.6, 3, 0.2)
bpy.ops.object.transform_apply()


def generate_colors():
    return (random.random(), random.random(), random.random(), 1.0)


angle_step = 3
current_angle = angle_step

while current_angle <= 360:
    bpy.ops.object.duplicate(linked=False)
    obj = bpy.context.active_object

    mats = bpy.data.materials.new(name=f"{current_angle}-mats")

    random_color = generate_colors()
    mats.diffuse_color = random_color

    if obj.data.materials:
        obj.data.materials[0] = mats
    else:
        obj.data.materials.append(mats)

    obj.location.z += obj.dimensions.z
    obj.rotation_euler.z = math.radians(current_angle)

    current_angle += angle_step
