import bpy
import math


radius_step = 0.1
current_radius = 0.1
number_triangles = 50

# for z rotation
z_step = 10

for i in range(number_triangles):
    current_radius = current_radius + radius_step
    # change vertices for different shapes like hexa
    bpy.ops.mesh.primitive_circle_add(vertices=3, radius=current_radius)

    triangle_mesh = bpy.context.active_object

    # x rotation
    degrees = -90
    radians = math.radians(degrees)
    triangle_mesh.rotation_euler.x = radians

    # z rotation
    degrees = z_step * i
    radians = math.radians(degrees)
    triangle_mesh.rotation_euler.z = radians

    bpy.ops.object.convert(target='CURVE')

    triangle_mesh.data.bevel_depth = 0.05
    triangle_mesh.data.bevel_resolution = 16

    bpy.ops.object.shade_smooth()